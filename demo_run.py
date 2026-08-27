"""
NexusML End-to-End Execution Demo
"""
import sys
from nexusml.core import Tensor, MatrixOps
from nexusml.data import StandardScaler, OneHotEncoder, FeatureStore, FeatureGroup
from nexusml.models import AutoMLPipeline, LogisticRegression, RandomForestClassifier, EvaluationReport
from nexusml.pipelines import DAGGraph, PipelineNode, AsyncPipelineRunner
from nexusml.registry import ModelRegistryStore, ExperimentTracker
from nexusml.serving import create_app, RealtimeInferenceEngine
from nexusml.dashboard import start_dashboard
from nexusml.utilities import get_logger, ExecutionTimer

logger = get_logger("NexusML-Demo")

def main():
    logger.info("=== NexusML Enterprise Platform Execution Demo ===")
    
    with ExecutionTimer():
        # 1. Feature Store & Preprocessing
        logger.info("Step 1: Initializing Feature Store & Data Preprocessing...")
        fs = FeatureStore()
        fg = FeatureGroup("customer_features", "customer_id")
        fs.register_feature_group(fg)
        fs.write_features("customer_features", "cust_1001", {"age": 34, "income": 75000.0, "score": 0.88})
        
        X_raw = [[25.0, 50000.0], [45.0, 120000.0], [35.0, 85000.0], [50.0, 150000.0]]
        y_raw = [0.0, 1.0, 0.0, 1.0]
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_raw)
        logger.info(f"Scaled dataset shape: ({len(X_scaled)}, {len(X_scaled[0])})")

        # 2. AutoML Model Search & Training
        logger.info("Step 2: Launching AutoML Pipeline Search...")
        automl = AutoMLPipeline(time_budget=30)
        predictions = automl.fit_predict(X_scaled, y_raw)
        accuracy = EvaluationReport.accuracy(y_raw, predictions)
        logger.info(f"AutoML Training Completed. Best Model: {automl.best_model.model_name}, Accuracy: {accuracy * 100:.1f}%")

        # 3. Model Registry & Experiment Tracking
        logger.info("Step 3: Registering Model Artifact & Logging Experiment...")
        tracker = ExperimentTracker("NexusML_Production_Exp")
        run_id = tracker.log_run({"lr": 0.01, "scaler": "StandardScaler"}, {"accuracy": accuracy})
        registry = ModelRegistryStore()
        registry.save_model("nexus_v1_prod", {"model_name": automl.best_model.model_name, "run_id": run_id})
        logger.info(f"Model saved to registry under run_id: {run_id}")

        # 4. DAG Pipeline Execution
        logger.info("Step 4: Executing Async DAG Pipeline...")
        graph = DAGGraph()
        n1 = PipelineNode("data_ingestion_node")
        n2 = PipelineNode("model_inference_node")
        graph.add_node(n1)
        graph.add_node(n2)
        runner = AsyncPipelineRunner(graph)
        dag_results = runner.run()
        logger.info(f"DAG Execution finished with node results: {list(dag_results.keys())}")

        # 5. Serving API & Microservices
        logger.info("Step 5: Initializing Real-time Inference Engine...")
        engine = RealtimeInferenceEngine()
        app_spec = create_app()
        logger.info(f"Serving Server Status: {app_spec['status']} (Version {app_spec['version']})")

        # 6. Web Dashboard Server
        logger.info("Step 6: Launching Web Dashboard...")
        start_dashboard(host="127.0.0.1", port=8000)

    logger.info("=== NexusML Execution Completed Successfully ===")

if __name__ == "__main__":
    main()

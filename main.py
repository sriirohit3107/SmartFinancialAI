import argparse
from modules.data_loader import fetch_and_process_data
from modules.model import load_model_and_predict
from modules.agent import generate_explanation
from modules.utils import display_prediction_summary


def main():
    parser = argparse.ArgumentParser(description="SmartFinancial AI Analyst")
    parser.add_argument("--ticker", type=str, help="Stock ticker symbol (e.g., AAPL)")
    parser.add_argument("--days", type=int, default=5, help="Number of days to predict")
    parser.add_argument("--window", type=int, default=30, help="Time window for input features")
    args = parser.parse_args()

    print(f"\n🚀 Starting prediction for {args.ticker}...")

    # Step 1: Fetch and preprocess data
    data, latest_window = fetch_and_process_data(args.ticker, window=args.window)

    # Step 2: Predict using ML model
    prediction = load_model_and_predict(args.ticker, latest_window, days=args.days)

    # Step 3: Generate explanation using LLM agent
    explanation = generate_explanation(args.ticker, prediction)

    # Step 4: Display result
    display_prediction_summary(args.ticker, prediction, explanation)


if __name__ == "__main__":
    main()

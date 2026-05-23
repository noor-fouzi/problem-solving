def aggregate_test_results(test_results):
    
    aggregated_test_results = {}

    for result in test_results:
        component = result.get("component")
        status = result.get("status")
        if component not in aggregated_test_results:
            aggregated_test_results.update({
                component: dict(
                    total_executed = 0,
                    passed_count = 0,
                    failed_count = 0,
                    pass_persentage = 0
            )})

        aggregated_test_results[component]["total_executed"] += 1

        if status == "PASS":
            aggregated_test_results[component]["passed_count"] += 1


        elif status == "FAIL":
            aggregated_test_results[component]["failed_count"] += 1

        total_executed = aggregated_test_results[component]["total_executed"]
        passed_count = aggregated_test_results[component]["passed_count"]
        aggregated_test_results[component]["pass_persentage"] = int(passed_count / total_executed * 100)

    return aggregated_test_results


if __name__ == "__main__":

    raw_test_results = [
        {"component": "Authentication", "test_name": "Verify_Valid_Login", "status": "PASS"},
        {"component": "Payment", "test_name": "Check_Credit_Card_Fail", "status": "FAIL"},
        {"component": "Authentication", "test_name": "SQL_Injection_Guard", "status": "PASS"},
        {"component": "Inventory", "test_name": "Update_Stock_Count", "status": "PASS"},
        {"component": "Payment", "test_name": "Apple_Pay_Integration", "status": "PASS"},
        {"component": "Authentication", "test_name": "Session_Timeout_Test", "status": "FAIL"}
    ]

    print(aggregate_test_results(raw_test_results))
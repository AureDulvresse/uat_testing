from app_tester import AppTester

def main():
    tester = AppTester("https://mak.digitaledge-drc.com", "aure", "Aure14902")
    tester.run_tests()

if __name__ == "__main__":
    main()

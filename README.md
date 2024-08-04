# Automatic Google Form Filler

## Overview
This project automates the process of filling out Google Forms using data extracted from a CSV file. It utilizes XPath to identify form fields and fill them automatically, making it an efficient tool for bulk submissions. The automation script runs in a Chrome browser environment, specifically tailored for developers.

## Features
- **Automatic Form Submission:** Fills out Google Forms automatically using data provided in a CSV file.
- **XPath Integration:** Utilizes XPath to accurately target and fill form fields.
- **Chrome Developer Tools:** Runs in Chrome, leveraging developer tools for enhanced control and debugging.

## Prerequisites
- **Google Chrome:** Ensure you have the latest version of Google Chrome installed.
- **ChromeDriver:** Compatible version with your Chrome browser. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

## Form
-**Form Used:** Example form [Form](https://docs.google.com/forms/d/e/1FAIpQLScsMrXjtSsg6sCI_zxNiyifWftniEReIi-tJFsKiI5uu3MTmw/viewform). You can use your own form, but update the XPath in the code respectively
 
## Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Vanshika689/automatic-google-form-filler.git
   cd google-form-filler
   ```

## Usage
### Prepare your CSV file
- Ensure your CSV file is formatted correctly with headers that match the expected input fields of the Google Form.

### Run the Script
```bash
python form_filler.py
```

## Check Results
Verify that the form submissions are correctly populated by checking the response sheet of the Google Form.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Contact
For questions or feedback, please reach out to me at [vanshiganjoo@example.com](mailto:vanshiganjoo@gmail.com).


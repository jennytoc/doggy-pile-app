import { Row, Col } from "react-bootstrap"
import './FooterStyles.css'
import Facebook from '../../images/facebook-icon.svg'
import Instagram from '../../images/instagram-icon.svg'
import Twitter from '../../images/twitter-icon.svg'

function Footer() {
  return (
    <footer>
      <Row className="footer-cont">
        <Col className="about-cont">
          <h3 className="footer-text mb-3">About Us</h3>
          <p align="left">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ac odio tempor orci dapibus ultrices in iaculis. Gravida cum sociis natoque penatibus et.</p>
        </Col>
        <Col>
          <h3 className="footer-text mb-3">Getting Started</h3>
          <p align="left">Sign Up</p>
        </Col>
        <Col>
          <h3 className="footer-text mb-3">Follow Us</h3>
          <Row>
            <img src={Facebook} alt="Facebook" className="footer-icons"/>
            <img src={Instagram} alt="Instagram" className="footer-icons"/>
            <img src={Twitter} alt="Twitter" className="footer-icons"/>
          </Row>
          <p align="left" className="mt-3">©DoggyPile. All rights reserved.</p>
        </Col>
      </Row>
    </footer>
  )
}

export default Footer;
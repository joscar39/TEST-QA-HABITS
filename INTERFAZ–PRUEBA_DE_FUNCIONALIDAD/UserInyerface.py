import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
# from selenium.webdriver.support.select import Select


class Juego_UserInyerface(unittest.TestCase):

    def setUp(self):
        path = r"C:\Users\user\Documents\Proyectos\Jmeter\INTERFAZ–PRUEBA_DE_FUNCIONALIDAD\Recursos\driver\driver.exe"
        self.driver = webdriver.Chrome(executable_path=path)

    def test_PlayGame(self):

        # ENTRAR AL HOME PAGE
        web = "https://userinyerface.com/"
        driver = self.driver
        driver.get(web)
        driver.maximize_window()

        # SELECCIONAR EL ENLACE PARA AVANZAR A INICIAR EL JUEGO
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "start__link").click()

        # CONDICIÓN PARA COMPROBAR SI EL MENSAJE DE COOKIES ESTA MOSTRÁNDOSE
        # DE SER CORRECTO PROCEDERÁ A CERRAR LA ALERTA DE COOKIES
        time.sleep(3)
        messagecookie = driver.find_element(By.CLASS_NAME, "cookies")
        if messagecookie.is_displayed():
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/div[1]/button").click()
        else:
            print("No hay alertas de cookies")

        filesheet = "C:/Users/user/Documents/Proyectos/Jmeter/INTERFAZ–PRUEBA_DE_FUNCIONALIDAD/Recursos/Datos.xlsx"
        wb = load_workbook(filesheet)
        datos = wb.get_sheet_by_name("Hoja1")

        for i in range(1, 4):

            password, email, domain = datos[f'A{i}:C{i}'][0]
            print(password.value, email.value, domain.value)
            time.sleep(1)
            # LIMPIAR LOS CAMPOS DEL TEXTO FIJO DEL PLACEHOLDER
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/div/div[1]/"
                                          "div/div[3]/form/div[1]/div[2]/input").clear()
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/div/div[1]/div/div[3]"
                                          "/form/div[1]/div[3]/div[1]/input").clear()
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/div/div[1]"
                                          "/div/div[3]/form/div[1]/div[3]/div[3]/input").clear()
            # INGRESAR LOS DATOS DE CONTRASEÑA Y CORREOS SUSTRAIDO DE EXCEL
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/div/div[1]"
                                          "/div/div[3]/form/div[1]/div[2]/input").send_keys(password.value)
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/div/div[1]/div"
                                          "/div[3]/form/div[1]/div[3]/div[1]/input").send_keys(email.value)
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/div/div[1]/div"
                                          "/div[3]/form/div[1]/div[3]/div[3]/input").send_keys(domain.value)

            # HACER UN CICLO FOR PARA BUSCAR ENTRE LA LISTA DE OPCIONES EL VALOR .COM

            # NO LOGRÉ REALIZAR LA BUSQUEDA DEL ELEMENTO DESPLEGABLE, PROVE CON SELECTORES DE CLASS, NAME, FULL XPATH
            # Y NINGUNA FUNCIONÓ EN TODAS LAS PRUEBAS SIEMPRE QUE SE TRATABA DE REALIZAR LA APERTURA DEL CAMPO SELECT
            # SE ROMPÍA LA AUTOMATIZACIÓN, VIENDO LA CONSOLA DE ERRORES ME PERCATÉ QUE EL MENSAJE
            # INDICABA QUE NO ERA UNA LISTA SELECT SINÓ UN DIV,
            # POR LO QUE PROCEDÍ A COMENTAR EL CÓDIGO DE SELECCIONAR UN VALOR DENTRO DE UNA LISTA
            # DESPLEGABLE Y SOLO CREE UN COMANDO QUE HAGA CLICK EN DOS ELEMENTOS,
            # EN PRIMERO ABRIRA LA LISTA Y EL SEGUNDO SELECCIONA LA OPCIÓN

            '''select = driver.find_element(By.CLASS_NAME, "dropdown__list-item")
            opcion = select.find_elements_by_css_selector("dropdown__list-item")
            time.sleep(2)
            for i in opcion:
                i.click()
                time.sleep(1)
            seleccionar = Select(select)
            seleccionar.select_by_value(".com")'''

            # SELECCIONAR UNA OPCION DE LA LISTA DESPLEGABLES DE OPCIONES, CABE DESTACAR QUE ESTOS ELEMENTOS NO ERAN
            # COINCIDENCIA DE BUSQUEDAS CON ELEMENTOS DE XPATH, CLASS, NAME, ID U OTRO SELECTOR
            # POR LO QUE SE PROCEDIO A UTILIZAR EL CSS SELECTOR
            driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > div:nth-child(4) > div >"
                                                 " div:nth-child(1) > div > div.login-form__container > form > "
                                                 "div.login-form__section.login-form__fields > div.align.align"
                                                 "--fluid.align--gutter-sm.login-form__field-row > div:nth-child(4)"
                                                 " > div > div.dropdown__header > div.dropdown__field").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > div:nth-child(4) > div > "
                                                 "div:nth-child(1) > div > div.login-form__container > form >"
                                                 " div.login-form__section.login-form__fields > div.align.align"
                                                 "--fluid.align--gutter-sm.login-form__field-row > div:nth-child(4)"
                                                 " > div > div.dropdown__list > div:nth-child(2)").click()
            time.sleep(1)

            # HACER CLICK EN CHECKBOX PARA DESMARCAR LOS TERMINOS Y CONDICIONES

            driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > "
                                                 "div:nth-child(4) > div > div:nth-child(1) >"
                                                 " div > div.login-form__container > form >"
                                                 " div:nth-child(2) > span > label > span >"
                                                 " span").click()
            time.sleep(1)

            # CONSULTAR SI EL CHECK DE TERMINOS Y CONDICIONES SE ENCUENTRA REALMENTE DESACTIVADO

            consulta = driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > "
                                                            "div:nth-child(4) > div > div:nth-child(1) >"
                                                            " div > div.login-form__container > form >"
                                                            " div:nth-child(2) > span > label > span >"
                                                            " span").is_selected()

            # VALIDANDO UNA CONDICION PARA EL CASO QUE EL CHECK DE TERMINOS Y CONDICIONES NO QUEDE SELECCIONADO

            if consulta is True:
                driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > "
                                                     "div:nth-child(4) > div > div:nth-child(1) >"
                                                     " div > div.login-form__container > form >"
                                                     " div:nth-child(2) > span > label > span >"
                                                     " span").click()
                time.sleep(1)

                print("El check de terminos se encuentra selecionado")
                driver.get_screenshot_as_file("C:\\Users\\user\\Documents\\Proyectos\\"
                                              "\\Jmeter\\INTERFAZ–PRUEBA_DE_FUNCIONALIDAD\\"
                                              "Recursos\\screenshots\\registrocorreo.png")

                driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > "
                                                     "div:nth-child(4) > div > div:nth-child(1) >"
                                                     " div > div.login-form__container > form >"
                                                     " div.login-form__section.align.align--"
                                                     "fluid.align--even > div:nth-child(1) > a").click()
                time.sleep(1)
            else:
                driver.get_screenshot_as_file("C:\\Users\\user\\Documents\\Proyectos\\"
                                              "\\Jmeter\\INTERFAZ–PRUEBA_DE_FUNCIONALIDAD\\"
                                              "Recursos\\screenshots\\registrocorreo.png")
                driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > "
                                                     "div:nth-child(4) > div > div:nth-child(1) >"
                                                     " div > div.login-form__container > form >"
                                                     " div.login-form__section.align.align--"
                                                     "fluid.align--even > div:nth-child(1) > a").click()
                time.sleep(2)

                print("Se pulsó el botón de siguiente")
                break
        # CARGAR UNA IMAGÉN EN EL INPUT DE AVATAR
        # NO SE LOGRO INGRESAR UNA IMAGEN PARA PROCEDER CON LA PRUEBA, EL INDICADOR
        # NO PERMITE ENVIAR DATOS YA QUE SE TRATA DE UNA ETIQUETA QUE HACE CARGA DE IMAGEN,
        # LO QUE NO PERMITE TRATARLO DE FORMA DIRECTA CON LA PAGINA WEB,
        # PARA REALIZAR ESTE PROCESO ES NECESARIO USAR HERRAMIENTAS EXTERNAS
        # QUE MANEJAN LOS RECURSOS DEL PROPIO SISTEMA OPERATIVO, ESAS HERRAMIENTAS PUEDEN SER:
        # AUTOIT, PYTHON PYWIN32 O SENDKEYS... SON ESTAS HARRAMIENTAS LAS QUE PODRIAN PERMITIR INTERACTUAR CON LA
        # VENTANA EMERGENTE DEL SISTEMA OPERATIVO Y HACER LA CARGA DE IMAGEN

        driver.find_element(By.CLASS_NAME, "avatar-and"
                                           "-interests__upload-button").send_keys(r"C:\\Users\\user\\Documents\\"
                                                                                  r"Proyectos\\Jmeter\\INTERFAZ"
                                                                                  r"–PRUEBA_DE_FUNCIONALIDAD\\"
                                                                                  r"Recursos\\avatar.png")
        time.sleep(5)

        # DESMARCAR TODOS LOS CHECK DE INTERESES
        unselect = driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content >"
                                                        " div:nth-child(4) > div > div.avatar-"
                                                        "and-interests > div > div.avatar-and-interests"
                                                        "__section.avatar-and-interests__interests-section"
                                                        " > div > div:nth-child(21) > div > span.checkbox."
                                                        "small > label > span")
        # SELECCIONAR LA OPCION DE DESMARCAR TODOS LOS CHECKS
        unselect.click()
        # ESCOGER PRIMER INTERES DE LAS MULTIPLES OPCIONES DE LA TABLA
        int1 = driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > div:nth-child(4)" 
                                                    " > div > div.avatar-and-interests > div > div.avatar" 
                                                    "-and-interests__section.avatar-and-interests__interests" 
                                                    "-section > div > div:nth-child(5) > div > span.checkbox.small" 
                                                    " > label > span")
        # CONSULTAR SI EL PRIMER CHECK DE INTERES ESTA MARCADO PREVIAMENTE
        marc1 = int1.is_selected()
        # ESCOGER SEGUNDO INTERES DE LAS MULTIPLES OPCIONES DE LA TABLA
        int2 = driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > div:nth-child(4)"
                                                    " > div > div.avatar-and-interests > div > "
                                                    "div.avatar-and-interests__section.avatar-and"
                                                    "-interests__interests-section > div > div:nth-child(11) "
                                                    "> div > span.checkbox.small > label > span")
        # CONSULTAR SI EL SEGUNDO CHECK DE INTERES ESTA MARCADO PREVIAMENTE
        marc2 = int2.is_selected()
        # ESCOGER TERCER INTERES DE LAS MULTIPLES OPCIONES DE LA TABLA
        int3 = driver.find_element(By.CSS_SELECTOR, "#app > div > div.view__content > div:nth-child(4) > div > "
                                                    "div.avatar-and-interests > div > div.avatar-and-"
                                                    "interests__section.avatar-and-interests__interests"
                                                    "-section > div > div:nth-child(17) > div > span."
                                                    "checkbox.small > label > span")
        # CONSULTAR SI EL TERCER CHECK DE INTERES ESTA MARCADO PREVIAMENTE
        marc3 = int3.is_selected()

        # REALIZAR CONDICION PARA VALIDAR SI LOS CHECK DE INTERES ESTAN
        # TODOS DISPONIBLES PARA MARCAR O SI YA ESTAN MARCADOS
        # SI CUMPLEN CON LA CONDICION DE QUE ESTAN DISPONIBLES SIN ESTAR SELECCIONADOS
        # SE PROCEDERA A HACER CLICK EN LOS INTERESES ESCOGIDOS Y POSTERIORMENTE SE PULSARA EL BOTON DE SIGUIENTE
        # SE ESTA TOMANDO UNA CAPTURA DE PANTALLA DONDE SE MUESTRA LOS INTERESES
        # SELECCIONADOS Y SE GUARDO EN LA CARPETA DE SCREENSHOT DEL APARTADO DE RECURSOS

        if marc1 & marc2 & marc3 is True:
            unselect.click()
            print("Se ha desmarcado todas las opciones de intereses")
            time.sleep(1)
            int1.click()
            time.sleep(1)
            int2.click()
            time.sleep(1)
            int3.click()
            print("Se seleccionaron 3 intereses de forma correcta")
            driver.get_screenshot_as_file("C:\\Users\\user\\Documents\\Proyectos\\"
                                          "\\Jmeter\\INTERFAZ–PRUEBA_DE_FUNCIONALIDAD\\"
                                          "Recursos\\screenshots\\selecciondeintereses.png")
            driver.find_element(By.CLASS_NAME, "button button--stroked button--white button--fluid").click()
            print("Se avanzó a la siguiente pantalla exitosamente")
        else:
            int1.click()
            time.sleep(1)
            int2.click()
            time.sleep(1)
            int3.click()
            print("Se seleccionaron 3 intereses de forma correcta")
            driver.get_screenshot_as_file("C:\\Users\\user\\Documents\\Proyectos\\"
                                          "\\Jmeter\\INTERFAZ–PRUEBA_DE_FUNCIONALIDAD\\"
                                          "Recursos\\screenshots\\selecciondeintereses.png")
            driver.find_element(By.CLASS_NAME, "button button--stroked button--white button--fluid").click()
            print("Se avanzó a la siguiente pantalla exitosamente")

        time.sleep(2)

        wb.close()

    def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
    unittest.main()

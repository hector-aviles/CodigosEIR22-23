# Introducción al desarrollo de vehículos sin conductor - Decisión de comportamientos
Escuela de Invierno de Robótica 2023

## Requerimientos:

* Ubuntu 20.04
* ROS Noetic
* Webots 2022a: https://github.com/cyberbotics/webots/releases/download/R2022a/webots_2022a_amd64.deb

## Instalación:

Nota: se asume que ya se tiene instalado Ubuntu y ROS.

* Seguir las instrucciones para instalar Webots usando un paquete Debian: https://cyberbotics.com/doc/guide/installing-webots
* Seguir el tutorial para el uso de Webots con ROS: https://cyberbotics.com/doc/guide/tutorial-9-using-ros
* $ cd
* $ git clone https://github.com/hector-aviles/CodigosEIR22-23
* $ cd CodigosEIR22-23
* $ cd catkin_ws
* $ catkin_make -j2 -l2
* $ echo "source ~/CodigosEIR22-23/catkin_ws/devel/setup.bash" >> ~/.bashrc
* $ source ~/.bashrc

## Prueba

Para probar que todo se instaló y compiló correctamente:

* roslaunch eir2023 navigation_no_obstacles.launch

Deberá aparecer un simulador como el siguiente:
<img src="https://github.com/hector-aviles/CodigosEIR22-23/blob/main/Media/Webots.png" alt="RViz" width="640"/>

## Tópicos relevantes

### Tópicos publicados:

* ``/camera/rgb/raw`` (sensor_msgs/Image): Imagen RGB de la cámara
* ``/point_cloud`` (sensor_msgs/PointCloud2): Nube de puntos generada por el Lidar

### Tópicos suscritos:

* ``/speed`` (std\_msgs/Float64): Velocidad lineal deseada en [km/h]
* ``/steering`` (std\_msgs/Float64): Ángulo de las llantas delanteras en [rad]

## Ejercicios

Se proporcionarán instrucciones para cada ejercicio que se verá durante el curso. Se puede ejecutar una demostración mediante el comando:

* roslaunch demo demo.launch

## Contacto

Dr. Héctor Avilés<br>
havilesa@upv.edu.mx 


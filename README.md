# 💸 Auto - Presupuesto

## ¿Qué es?
El "Auto-presupuesto" es una herramienta para crear un presupuesto de forma automática en función de una base de datos con presupuestos de proyectos similares y el número de módulos solares.

## ¿Qué se necesita para que funcione?
El corazón de la herramienta es su base de datos, por lo que será necesario tener algunos presupuestos de referencia introducidos bien desde el admin de Django o desde la herramienta en si, usando su variable "Oferta Real"

## ¿Cómo utilizarla?
Deberás introducir cada una de las variables que te pidan para caracterizar el proyecto (tipo de integración, transporte, número de mósulods, fluido, etc) y se creará una curva de coste con los proyectos existentes similares de la base de datos. El presupuesto se creará finalmente en función del número de módulos del proyecto como variable principal.

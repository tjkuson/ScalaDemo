package scalademo.syntax

class UpperDemo:
  def convert(strings: Seq[String]): Seq[String] =
    strings.map((s: String) => s.toUpperCase)

object Demo:
  @main def Hello(): Unit =
    val up = new UpperDemo()
    val strings = List("Hello", "Xander!")
    val result = up.convert(strings).mkString(" ")
    println(result)
package scalademo.patternmatching

sealed trait Animal

case class Human(name: String) extends Animal

case class Dog(is_big: Boolean) extends Animal

case class Cat() extends Animal

object ProcessAnimals:
  def apply(animal: Animal): String =
    animal match
      case Human(name) => s"Hello, my name is $name"
      case Dog(true) => "Woof"
      case Dog(false) => "Yip"
      case Cat() => "Meow"

  @main def main(): Unit =
    val animals = List(Human("John"), Dog(true), Dog(false), Cat())
    animals.foreach { animal => println(ProcessAnimals(animal)) }
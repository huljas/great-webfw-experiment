class MainController < ApplicationController
 
  def fibo
    @result = Fibonacci.fibonacci(Integer(params[:n]))
  end

end

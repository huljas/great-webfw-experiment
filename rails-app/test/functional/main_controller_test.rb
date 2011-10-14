require 'test_helper'

class MainControllerTest < ActionController::TestCase
  test "should get fibo" do
    get :fibo
    assert_response :success
  end

end

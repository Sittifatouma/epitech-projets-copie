defmodule TodolistWeb.RoleControllerTest do
  use TodolistWeb.ConnCase

  import Todolist.TmanageFixtures

  alias Todolist.Tmanage.Role

  @create_attrs %{
    email: "some email",
    role: "some role",
    username: "some username"
  }
  @update_attrs %{
    email: "some updated email",
    role: "some updated role",
    username: "some updated username"
  }
  @invalid_attrs %{email: nil, role: nil, username: nil}

  setup %{conn: conn} do
    {:ok, conn: put_req_header(conn, "accept", "application/json")}
  end

  describe "index" do
    test "lists all roles", %{conn: conn} do
      conn = get(conn, Routes.role_path(conn, :index))
      assert json_response(conn, 200)["data"] == []
    end
  end

  describe "create role" do
    test "renders role when data is valid", %{conn: conn} do
      conn = post(conn, Routes.role_path(conn, :create), role: @create_attrs)
      assert %{"id" => id} = json_response(conn, 201)["data"]

      conn = get(conn, Routes.role_path(conn, :show, id))

      assert %{
               "id" => ^id,
               "email" => "some email",
               "role" => "some role",
               "username" => "some username"
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn} do
      conn = post(conn, Routes.role_path(conn, :create), role: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "update role" do
    setup [:create_role]

    test "renders role when data is valid", %{conn: conn, role: %Role{id: id} = role} do
      conn = put(conn, Routes.role_path(conn, :update, role), role: @update_attrs)
      assert %{"id" => ^id} = json_response(conn, 200)["data"]

      conn = get(conn, Routes.role_path(conn, :show, id))

      assert %{
               "id" => ^id,
               "email" => "some updated email",
               "role" => "some updated role",
               "username" => "some updated username"
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn, role: role} do
      conn = put(conn, Routes.role_path(conn, :update, role), role: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "delete role" do
    setup [:create_role]

    test "deletes chosen role", %{conn: conn, role: role} do
      conn = delete(conn, Routes.role_path(conn, :delete, role))
      assert response(conn, 204)

      assert_error_sent 404, fn ->
        get(conn, Routes.role_path(conn, :show, role))
      end
    end
  end

  defp create_role(_) do
    role = role_fixture()
    %{role: role}
  end
end

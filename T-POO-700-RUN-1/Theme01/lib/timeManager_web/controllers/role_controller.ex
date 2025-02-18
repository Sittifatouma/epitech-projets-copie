defmodule TodolistWeb.RoleController do
  use TodolistWeb, :controller

  alias Todolist.Tmanage
  alias Todolist.Tmanage.Role

  action_fallback TodolistWeb.FallbackController

  def index(conn, _params) do
    roles = Tmanage.list_roles()
    render(conn, "index.json", roles: roles)
  end

  def create(conn, %{"role" => role_params}) do
    with {:ok, %Role{} = role} <- Tmanage.create_role(role_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.role_path(conn, :show, role))
      |> render("show.json", role: role)
    end
  end

  def show(conn, %{"id" => id}) do
    role = Tmanage.get_role!(id)
    render(conn, "show.json", role: role)
  end

  def update(conn, %{"id" => id, "role" => role_params}) do
    role = Tmanage.get_role!(id)

    with {:ok, %Role{} = role} <- Tmanage.update_role(role, role_params) do
      render(conn, "show.json", role: role)
    end
  end

  def delete(conn, %{"id" => id}) do
    role = Tmanage.get_role!(id)

    with {:ok, %Role{}} <- Tmanage.delete_role(role) do
      send_resp(conn, :no_content, "")
    end
  end
end

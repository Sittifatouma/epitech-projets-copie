defmodule TodolistWeb.RoleView do
  use TodolistWeb, :view
  alias TodolistWeb.RoleView

  def render("index.json", %{roles: roles}) do
    %{data: render_many(roles, RoleView, "role.json")}
  end

  def render("show.json", %{role: role}) do
    %{data: render_one(role, RoleView, "role.json")}
  end

  def render("role.json", %{role: role}) do
    %{
      id: role.id,
      username: role.username,
      email: role.email,
      role: role.role
    }
  end
end

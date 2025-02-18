defmodule Todolist.Tmanage.Role do
  use Ecto.Schema
  import Ecto.Changeset

  schema "roles" do
    field :email, :string
    field :role, :string
    field :username, :string

    timestamps()
  end

  @doc false
  def changeset(role, attrs) do
    role
    |> cast(attrs, [:username, :email, :role])
    |> validate_required([:username, :email, :role])
    |> unique_constraint(:email)
    |> unique_constraint(:username)
  end
end

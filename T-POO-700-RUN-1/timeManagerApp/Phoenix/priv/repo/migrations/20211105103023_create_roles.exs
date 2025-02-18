defmodule Todolist.Repo.Migrations.CreateRoles do
  use Ecto.Migration

  def change do
    create table(:roles) do
      add :username, :string
      add :email, :string
      add :role, :string

      timestamps()
    end

    create unique_index(:roles, [:email])
    create unique_index(:roles, [:username])
  end
end

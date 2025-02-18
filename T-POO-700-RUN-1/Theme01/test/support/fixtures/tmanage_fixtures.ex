defmodule Todolist.TmanageFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `Todolist.Tmanage` context.
  """

  @doc """
  Generate a clock.
  """
  def clock_fixture(attrs \\ %{}) do
    {:ok, clock} =
      attrs
      |> Enum.into(%{
        status: true,
        time: ~N[2021-11-04 10:20:00],
        user_id: 42
      })
      |> Todolist.Tmanage.create_clock()

    clock
  end

  @doc """
  Generate a workingtime.
  """
  def workingtime_fixture(attrs \\ %{}) do
    {:ok, workingtime} =
      attrs
      |> Enum.into(%{
        end: ~N[2021-11-04 10:29:00],
        start: ~N[2021-11-04 10:29:00],
        user_id: 42
      })
      |> Todolist.Tmanage.create_workingtime()

    workingtime
  end

  @doc """
  Generate a unique role email.
  """
  def unique_role_email, do: "some email#{System.unique_integer([:positive])}"

  @doc """
  Generate a unique role username.
  """
  def unique_role_username, do: "some username#{System.unique_integer([:positive])}"

  @doc """
  Generate a role.
  """
  def role_fixture(attrs \\ %{}) do
    {:ok, role} =
      attrs
      |> Enum.into(%{
        email: unique_role_email(),
        role: "some role",
        username: unique_role_username()
      })
      |> Todolist.Tmanage.create_role()

    role
  end
end

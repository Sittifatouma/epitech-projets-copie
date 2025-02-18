defmodule Todolist.TmanageFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `Todolist.Tmanage` context.
  """

  @doc """
  Generate a unique user email.
  """
  def unique_user_email, do: "some email#{System.unique_integer([:positive])}"

  @doc """
  Generate a unique user username.
  """
  def unique_user_username, do: "some username#{System.unique_integer([:positive])}"

  @doc """
  Generate a user.
  """
  def user_fixture(attrs \\ %{}) do
    {:ok, user} =
      attrs
      |> Enum.into(%{
        email: unique_user_email(),
        username: unique_user_username()
      })
      |> Todolist.Tmanage.create_user()

    user
  end

  @doc """
  Generate a clock.
  """
  def clock_fixture(attrs \\ %{}) do
    {:ok, clock} =
      attrs
      |> Enum.into(%{
        status: true,
        time: ~N[2021-10-31 05:59:00]
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
        end: ~N[2021-10-31 06:00:00],
        start: ~N[2021-10-31 06:00:00]
      })
      |> Todolist.Tmanage.create_workingtime()

    workingtime
  end
end

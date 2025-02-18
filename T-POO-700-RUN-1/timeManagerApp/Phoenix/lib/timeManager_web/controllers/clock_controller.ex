defmodule TodolistWeb.ClockController do
  use TodolistWeb, :controller

  alias Todolist.Tmanage
  alias Todolist.Tmanage.Clock

  action_fallback TodolistWeb.FallbackController

  def index(conn, _params) do
    clocks = Tmanage.list_clocks()
    render(conn, "index.json", clocks: clocks)
  end

  def create(conn, %{"clock" => clock_params}) do
    with {:ok, %Clock{} = clock} <- Tmanage.create_clock(clock_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.clock_path(conn, :show, clock))
      |> render("show.json", clock: clock)
    end
  end

  def show(conn, %{"id" => id}) do
    clock = Tmanage.get_clock!(id)
    render(conn, "show.json", clock: clock)
  end

  def update(conn, %{"id" => id, "clock" => clock_params}) do
    clock = Tmanage.get_clock!(id)

    with {:ok, %Clock{} = clock} <- Tmanage.update_clock(clock, clock_params) do
      render(conn, "show.json", clock: clock)
    end
  end

  def delete(conn, %{"id" => id}) do
    clock = Tmanage.get_clock!(id)

    with {:ok, %Clock{}} <- Tmanage.delete_clock(clock) do
      send_resp(conn, :no_content, "")
    end
  end
end

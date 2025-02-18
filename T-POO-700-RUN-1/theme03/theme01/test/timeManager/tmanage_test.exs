defmodule Todolist.TmanageTest do
  use Todolist.DataCase

  alias Todolist.Tmanage

  describe "users" do
    alias Todolist.Tmanage.User

    import Todolist.TmanageFixtures

    @invalid_attrs %{email: nil, username: nil}

    test "list_users/0 returns all users" do
      user = user_fixture()
      assert Tmanage.list_users() == [user]
    end

    test "get_user!/1 returns the user with given id" do
      user = user_fixture()
      assert Tmanage.get_user!(user.id) == user
    end

    test "create_user/1 with valid data creates a user" do
      valid_attrs = %{email: "some email", username: "some username"}

      assert {:ok, %User{} = user} = Tmanage.create_user(valid_attrs)
      assert user.email == "some email"
      assert user.username == "some username"
    end

    test "create_user/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Tmanage.create_user(@invalid_attrs)
    end

    test "update_user/2 with valid data updates the user" do
      user = user_fixture()
      update_attrs = %{email: "some updated email", username: "some updated username"}

      assert {:ok, %User{} = user} = Tmanage.update_user(user, update_attrs)
      assert user.email == "some updated email"
      assert user.username == "some updated username"
    end

    test "update_user/2 with invalid data returns error changeset" do
      user = user_fixture()
      assert {:error, %Ecto.Changeset{}} = Tmanage.update_user(user, @invalid_attrs)
      assert user == Tmanage.get_user!(user.id)
    end

    test "delete_user/1 deletes the user" do
      user = user_fixture()
      assert {:ok, %User{}} = Tmanage.delete_user(user)
      assert_raise Ecto.NoResultsError, fn -> Tmanage.get_user!(user.id) end
    end

    test "change_user/1 returns a user changeset" do
      user = user_fixture()
      assert %Ecto.Changeset{} = Tmanage.change_user(user)
    end
  end

  describe "clocks" do
    alias Todolist.Tmanage.Clock

    import Todolist.TmanageFixtures

    @invalid_attrs %{status: nil, time: nil}

    test "list_clocks/0 returns all clocks" do
      clock = clock_fixture()
      assert Tmanage.list_clocks() == [clock]
    end

    test "get_clock!/1 returns the clock with given id" do
      clock = clock_fixture()
      assert Tmanage.get_clock!(clock.id) == clock
    end

    test "create_clock/1 with valid data creates a clock" do
      valid_attrs = %{status: true, time: ~N[2021-10-31 05:59:00]}

      assert {:ok, %Clock{} = clock} = Tmanage.create_clock(valid_attrs)
      assert clock.status == true
      assert clock.time == ~N[2021-10-31 05:59:00]
    end

    test "create_clock/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Tmanage.create_clock(@invalid_attrs)
    end

    test "update_clock/2 with valid data updates the clock" do
      clock = clock_fixture()
      update_attrs = %{status: false, time: ~N[2021-11-01 05:59:00]}

      assert {:ok, %Clock{} = clock} = Tmanage.update_clock(clock, update_attrs)
      assert clock.status == false
      assert clock.time == ~N[2021-11-01 05:59:00]
    end

    test "update_clock/2 with invalid data returns error changeset" do
      clock = clock_fixture()
      assert {:error, %Ecto.Changeset{}} = Tmanage.update_clock(clock, @invalid_attrs)
      assert clock == Tmanage.get_clock!(clock.id)
    end

    test "delete_clock/1 deletes the clock" do
      clock = clock_fixture()
      assert {:ok, %Clock{}} = Tmanage.delete_clock(clock)
      assert_raise Ecto.NoResultsError, fn -> Tmanage.get_clock!(clock.id) end
    end

    test "change_clock/1 returns a clock changeset" do
      clock = clock_fixture()
      assert %Ecto.Changeset{} = Tmanage.change_clock(clock)
    end
  end

  describe "workingtimes" do
    alias Todolist.Tmanage.Workingtime

    import Todolist.TmanageFixtures

    @invalid_attrs %{end: nil, start: nil}

    test "list_workingtimes/0 returns all workingtimes" do
      workingtime = workingtime_fixture()
      assert Tmanage.list_workingtimes() == [workingtime]
    end

    test "get_workingtime!/1 returns the workingtime with given id" do
      workingtime = workingtime_fixture()
      assert Tmanage.get_workingtime!(workingtime.id) == workingtime
    end

    test "create_workingtime/1 with valid data creates a workingtime" do
      valid_attrs = %{end: ~N[2021-10-31 06:00:00], start: ~N[2021-10-31 06:00:00]}

      assert {:ok, %Workingtime{} = workingtime} = Tmanage.create_workingtime(valid_attrs)
      assert workingtime.end == ~N[2021-10-31 06:00:00]
      assert workingtime.start == ~N[2021-10-31 06:00:00]
    end

    test "create_workingtime/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Tmanage.create_workingtime(@invalid_attrs)
    end

    test "update_workingtime/2 with valid data updates the workingtime" do
      workingtime = workingtime_fixture()
      update_attrs = %{end: ~N[2021-11-01 06:00:00], start: ~N[2021-11-01 06:00:00]}

      assert {:ok, %Workingtime{} = workingtime} = Tmanage.update_workingtime(workingtime, update_attrs)
      assert workingtime.end == ~N[2021-11-01 06:00:00]
      assert workingtime.start == ~N[2021-11-01 06:00:00]
    end

    test "update_workingtime/2 with invalid data returns error changeset" do
      workingtime = workingtime_fixture()
      assert {:error, %Ecto.Changeset{}} = Tmanage.update_workingtime(workingtime, @invalid_attrs)
      assert workingtime == Tmanage.get_workingtime!(workingtime.id)
    end

    test "delete_workingtime/1 deletes the workingtime" do
      workingtime = workingtime_fixture()
      assert {:ok, %Workingtime{}} = Tmanage.delete_workingtime(workingtime)
      assert_raise Ecto.NoResultsError, fn -> Tmanage.get_workingtime!(workingtime.id) end
    end

    test "change_workingtime/1 returns a workingtime changeset" do
      workingtime = workingtime_fixture()
      assert %Ecto.Changeset{} = Tmanage.change_workingtime(workingtime)
    end
  end
end

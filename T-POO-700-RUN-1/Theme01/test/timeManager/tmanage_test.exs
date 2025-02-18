defmodule Todolist.TmanageTest do
  use Todolist.DataCase

  alias Todolist.Tmanage

  describe "clocks" do
    alias Todolist.Tmanage.Clock

    import Todolist.TmanageFixtures

    @invalid_attrs %{status: nil, time: nil, user_id: nil}

    test "list_clocks/0 returns all clocks" do
      clock = clock_fixture()
      assert Tmanage.list_clocks() == [clock]
    end

    test "get_clock!/1 returns the clock with given id" do
      clock = clock_fixture()
      assert Tmanage.get_clock!(clock.id) == clock
    end

    test "create_clock/1 with valid data creates a clock" do
      valid_attrs = %{status: true, time: ~N[2021-11-04 10:20:00], user_id: 42}

      assert {:ok, %Clock{} = clock} = Tmanage.create_clock(valid_attrs)
      assert clock.status == true
      assert clock.time == ~N[2021-11-04 10:20:00]
      assert clock.user_id == 42
    end

    test "create_clock/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Tmanage.create_clock(@invalid_attrs)
    end

    test "update_clock/2 with valid data updates the clock" do
      clock = clock_fixture()
      update_attrs = %{status: false, time: ~N[2021-11-05 10:20:00], user_id: 43}

      assert {:ok, %Clock{} = clock} = Tmanage.update_clock(clock, update_attrs)
      assert clock.status == false
      assert clock.time == ~N[2021-11-05 10:20:00]
      assert clock.user_id == 43
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

    @invalid_attrs %{end: nil, start: nil, user_id: nil}

    test "list_workingtimes/0 returns all workingtimes" do
      workingtime = workingtime_fixture()
      assert Tmanage.list_workingtimes() == [workingtime]
    end

    test "get_workingtime!/1 returns the workingtime with given id" do
      workingtime = workingtime_fixture()
      assert Tmanage.get_workingtime!(workingtime.id) == workingtime
    end

    test "create_workingtime/1 with valid data creates a workingtime" do
      valid_attrs = %{end: ~N[2021-11-04 10:29:00], start: ~N[2021-11-04 10:29:00], user_id: 42}

      assert {:ok, %Workingtime{} = workingtime} = Tmanage.create_workingtime(valid_attrs)
      assert workingtime.end == ~N[2021-11-04 10:29:00]
      assert workingtime.start == ~N[2021-11-04 10:29:00]
      assert workingtime.user_id == 42
    end

    test "create_workingtime/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Tmanage.create_workingtime(@invalid_attrs)
    end

    test "update_workingtime/2 with valid data updates the workingtime" do
      workingtime = workingtime_fixture()
      update_attrs = %{end: ~N[2021-11-05 10:29:00], start: ~N[2021-11-05 10:29:00], user_id: 43}

      assert {:ok, %Workingtime{} = workingtime} = Tmanage.update_workingtime(workingtime, update_attrs)
      assert workingtime.end == ~N[2021-11-05 10:29:00]
      assert workingtime.start == ~N[2021-11-05 10:29:00]
      assert workingtime.user_id == 43
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

  describe "roles" do
    alias Todolist.Tmanage.Role

    import Todolist.TmanageFixtures

    @invalid_attrs %{email: nil, role: nil, username: nil}

    test "list_roles/0 returns all roles" do
      role = role_fixture()
      assert Tmanage.list_roles() == [role]
    end

    test "get_role!/1 returns the role with given id" do
      role = role_fixture()
      assert Tmanage.get_role!(role.id) == role
    end

    test "create_role/1 with valid data creates a role" do
      valid_attrs = %{email: "some email", role: "some role", username: "some username"}

      assert {:ok, %Role{} = role} = Tmanage.create_role(valid_attrs)
      assert role.email == "some email"
      assert role.role == "some role"
      assert role.username == "some username"
    end

    test "create_role/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Tmanage.create_role(@invalid_attrs)
    end

    test "update_role/2 with valid data updates the role" do
      role = role_fixture()
      update_attrs = %{email: "some updated email", role: "some updated role", username: "some updated username"}

      assert {:ok, %Role{} = role} = Tmanage.update_role(role, update_attrs)
      assert role.email == "some updated email"
      assert role.role == "some updated role"
      assert role.username == "some updated username"
    end

    test "update_role/2 with invalid data returns error changeset" do
      role = role_fixture()
      assert {:error, %Ecto.Changeset{}} = Tmanage.update_role(role, @invalid_attrs)
      assert role == Tmanage.get_role!(role.id)
    end

    test "delete_role/1 deletes the role" do
      role = role_fixture()
      assert {:ok, %Role{}} = Tmanage.delete_role(role)
      assert_raise Ecto.NoResultsError, fn -> Tmanage.get_role!(role.id) end
    end

    test "change_role/1 returns a role changeset" do
      role = role_fixture()
      assert %Ecto.Changeset{} = Tmanage.change_role(role)
    end
  end
end

def test_main_runs_and_exits(monkeypatch, capsys):
    inputs = iter(["R", "Q"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from main import main
    main()
    output = capsys.readouterr().out
    assert "Welcome to Rock Paper Scissors!" in output
    assert "Choose [R]ock [P]aper or [S]cissors. [Q]uit." in output
    assert "AI played:" in output
    assert "Final score:" in output

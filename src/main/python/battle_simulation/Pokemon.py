import pandas as pd
import os
from pathlib import Path
import battle_simulation.constants as const
import random


class Pokemon:

    def __init__(self, name, pokemon_info_df, moveset):
        """

        Args:
            name:
            pokemon_info_df:
            moveset: <dict> of the moveset, can only contain damage causing moves currently.  4 moves max.
            {1: {'Confusion': {'power':50, 'accuracy':100}}}
        """
        self.name = name
        self.hp = pokemon_info_df.loc[name, const.HP]
        self.attack = pokemon_info_df.loc[name, const.ATTACK]
        self.defense = pokemon_info_df.loc[name, const.DEFENSE]
        self.speed = pokemon_info_df.loc[name, const.SPEED]
        self.moveset = moveset

    # todo add ability and effects to use status changing moves
    def take_damage(self, other_pokemon, move_damage):
        """
        Current Pokemon takes damage from an opposing one
        Assume damage initially set to 100 with contributions from current Pokemon's defense and opposing one's attack

        Args:
            other_pokemon: <Pokemon> Pokemon that is inflicting damage on current one
            move_damage: <int> Power factor of the move that the other Pokemon is using to inflict damage on current one
        """
        # assume equal contributions
        # from move power: 0.5 * (move_power/100) * 100
        damage = max((0.5 * move_damage) + (0.5 * (other_pokemon.attack - self.defense)),
                     0)  # Needs to be positive damage

        self.hp = max(self.hp - damage, 0)

        if self.hp == 0:
            print('{name} has fainted.'.format(name=self.name))
            print('{other_name} is the winner.'.format(other_name=other_pokemon.name))
        else:
            print('{name} HP is now {hp}.'.format(name=self.name, hp=self.hp))

    def use_move(self, other_pokemon):
        """

        Args:
            other_pokemon:

        Returns:

        """
        # todo need to account for move accuracy.  Right now, everything is just 100%
        # choose random move to use
        move_dict = self.moveset[random.randint(1, 4)]  # {'Confusion': {'power':50, 'accuracy':100}}
        move_name = list(move_dict.keys())[0]
        print('{name} used {move_name}!'.format(name=self.name, move_name=move_name))
        other_pokemon.take_damage(self, move_dict[move_name][const.POW])
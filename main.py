def build_trade_centre():
    # FLOOR (5x5)
    blocks.place(IRON_BLOCK, positions.create(0,0,0))
    blocks.place(IRON_BLOCK, positions.create(1,0,0))
    blocks.place(IRON_BLOCK, positions.create(2,0,0))
    blocks.place(IRON_BLOCK, positions.create(3,0,0))
    blocks.place(IRON_BLOCK, positions.create(4,0,0))
    
    blocks.place(IRON_BLOCK, positions.create(0,0,1))
    blocks.place(IRON_BLOCK, positions.create(1,0,1))
    blocks.place(IRON_BLOCK, positions.create(2,0,1))
    blocks.place(IRON_BLOCK, positions.create(3,0,1))
    blocks.place(IRON_BLOCK, positions.create(4,0,1))
    
    blocks.place(IRON_BLOCK, positions.create(0,0,2))
    blocks.place(IRON_BLOCK, positions.create(1,0,2))
    blocks.place(IRON_BLOCK, positions.create(2,0,2))
    blocks.place(IRON_BLOCK, positions.create(3,0,2))
    blocks.place(IRON_BLOCK, positions.create(4,0,2))
    
    blocks.place(IRON_BLOCK, positions.create(0,0,3))
    blocks.place(IRON_BLOCK, positions.create(1,0,3))
    blocks.place(IRON_BLOCK, positions.create(2,0,3))
    blocks.place(IRON_BLOCK, positions.create(3,0,3))
    blocks.place(IRON_BLOCK, positions.create(4,0,3))
    
    blocks.place(IRON_BLOCK, positions.create(0,0,4))
    blocks.place(IRON_BLOCK, positions.create(1,0,4))
    blocks.place(IRON_BLOCK, positions.create(2,0,4))
    blocks.place(IRON_BLOCK, positions.create(3,0,4))
    blocks.place(IRON_BLOCK, positions.create(4,0,4))

    # WALLS (height 3)
    # NORTH wall
    blocks.place(STONE_BRICKS, positions.create(0,1,0))
    blocks.place(STONE_BRICKS, positions.create(1,1,0))
    blocks.place(STONE_BRICKS, positions.create(2,1,0))
    blocks.place(STONE_BRICKS, positions.create(3,1,0))
    blocks.place(STONE_BRICKS, positions.create(4,1,0))
    
    blocks.place(STONE_BRICKS, positions.create(0,2,0))
    blocks.place(STONE_BRICKS, positions.create(1,2,0))
    blocks.place(STONE_BRICKS, positions.create(2,2,0))
    blocks.place(STONE_BRICKS, positions.create(3,2,0))
    blocks.place(STONE_BRICKS, positions.create(4,2,0))
    
    blocks.place(STONE_BRICKS, positions.create(0,3,0))
    blocks.place(STONE_BRICKS, positions.create(1,3,0))
    blocks.place(STONE_BRICKS, positions.create(2,3,0))
    blocks.place(STONE_BRICKS, positions.create(3,3,0))
    blocks.place(STONE_BRICKS, positions.create(4,3,0))

    # EAST wall
    blocks.place(STONE_BRICKS, positions.create(4,1,1))
    blocks.place(STONE_BRICKS, positions.create(4,2,1))
    blocks.place(STONE_BRICKS, positions.create(4,3,1))
    
    blocks.place(STONE_BRICKS, positions.create(4,1,2))
    blocks.place(STONE_BRICKS, positions.create(4,2,2))
    blocks.place(STONE_BRICKS, positions.create(4,3,2))
    
    blocks.place(STONE_BRICKS, positions.create(4,1,3))
    blocks.place(STONE_BRICKS, positions.create(4,2,3))
    blocks.place(STONE_BRICKS, positions.create(4,3,3))

    # WEST wall
    blocks.place(STONE_BRICKS, positions.create(0,1,1))
    blocks.place(STONE_BRICKS, positions.create(0,2,1))
    blocks.place(STONE_BRICKS, positions.create(0,3,1))
    
    blocks.place(STONE_BRICKS, positions.create(0,1,2))
    blocks.place(STONE_BRICKS, positions.create(0,2,2))
    blocks.place(STONE_BRICKS, positions.create(0,3,2))
    
    blocks.place(STONE_BRICKS, positions.create(0,1,3))
    blocks.place(STONE_BRICKS, positions.create(0,2,3))
    blocks.place(STONE_BRICKS, positions.create(0,3,3))

    # COUNTERS (trade items)
    blocks.place(GOLD_BLOCK, positions.create(1,1,1))
    blocks.place(DIAMOND_BLOCK, positions.create(2,1,1))
    blocks.place(EMERALD_BLOCK, positions.create(3,1,1))

    blocks.place(REDSTONE_BLOCK, positions.create(1,1,2))
    blocks.place(LAPIS_LAZULI_BLOCK, positions.create(2,1,2))
    blocks.place(COAL_BLOCK, positions.create(3,1,2))

    # OPTIONAL: small decorative tower in center
    blocks.place(GLASS, positions.create(2,2,2))

player.on_chat("tradecentre", build_trade_centre)

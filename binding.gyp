{
  "targets": [
    {
      "target_name": "node_dht_sensor",
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "sources": [
        "src/bcm2835.c",
        "src/node-dht-sensor.cpp"
      ]
    }
  ]
}
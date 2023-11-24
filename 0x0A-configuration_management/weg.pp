# manifest.pp

package { 'werkzeug':
  ensure   => '2.1.1', # Replace with the version you need
  provider => 'pip3',
}

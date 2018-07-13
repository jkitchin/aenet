  ! Print NNs


program print_nns
  use feedforward, only: Network,                &
       load_Network, &
       ff_print_info

  character(len=1024) :: infile

  call initialize(infile)

contains

  subroutine initialize (infile)
    character(len=*) :: infile
    type(Network) :: net
    character(len=100) :: fname
    call get_command_argument(1, value=infile)
    net = load_Network(infile)
    write(*,*) "Summary of ", infile
    write(*,'(1x,"Number of layers : ",I3)') net%nlayers
    write(*,*)
    write(*,'(1x,"Number of nodes (without bias) ")')
    write(*,'(1x,"and activation type per layer :")')
    write(*,*)
    write(*,'(5x,I3," : ",I5)') 1, net%nnodes(1)
    do ilayer = 2, net%nlayers
       select case(net%f_a(ilayer))
       case(0)
          fname = 'linear function (linear)'
       case(1)
          fname = 'hyperbolic tangent (tanh)'
       case(2)
          fname = 'logistic function (sigmoid)'
       case(3)
          fname = 'scaled hyperbolic tangent (mtanh)'
       case(4)
          fname = 'scaled hyperbolic tangent + linear twisting (twist)'
       case(5)
          fname = 'rectified linear unit (relu)'
       case(6)
          fname = 'sigmoid-weighted linear unit (swish)'
       end select
       write(*,'(5x,I3," : ",I5,2x,A)') ilayer, net%nnodes(ilayer), trim(fname)
    end do
    write(*,*)

    write(*,'(1x,"Required memory (words) : ",I10," (",F10.2," KB)")') &
         net%memsize, dble(net%memsize*8)/1024.0d0
    write(*,*)

    write(*,'(1x,"Total number of weights (incl. bias) : ",I8)') net%Wsize
    write(*,*)


    write(*,'(1x,"Weight matrices:")')
    write(*,*)

    iw1 = 1
    do ilayer = 1, net%nlayers-1
       iw2 = net%iw(ilayer+1)
       call print_mat(reshape(net%W(iw1:iw2), &
            (/net%nnodes(ilayer+1),net%nnodes(ilayer)+1/) ))
       write(*,*)
    end do

  end subroutine initialize


  subroutine print_mat(A)

    implicit none

    double precision, dimension(:,:), intent(in) :: A

    integer                     :: n1, n2
    integer                     :: i1, i2

    double precision            :: val
    double precision, parameter :: EPS = 1.0d-12

    n1 = size(A(:,1))
    n2 = size(A(1,:))

    do i1 = 1, n1
       do i2 = 1, n2
          val = A(i1,i2)
          if (abs(val) < EPS) val = 0.0d0
          write(*, '(1x,F6.3,2x)', advance='no') val
       end do
       write(*,*)
    end do

  end subroutine print_mat

end program print_nns

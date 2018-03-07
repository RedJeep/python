from lineSegments import*
from bridgeparts import*


def lightSingleSpan():
    ''' prints the light span bridge'''
    print ("Single Span, Heavy Roadway Bridge:")
    print
    print singleSpanLightRoadwayLayer( )
    print singleSpanSupportLayer( )
    print  singleSpanSupportLayer( )
    print singleSpanSupportLayer( )

def heavySingleSpan():
    ''' displays heavy span bridge'''
    print ("Single Span, Heavy Roadway Bridge:")
    print 
    print singleSpanHeavyRoadwayLayer( )
    print singleSpanSupportLayer( )
    print singleSpanSupportLayer( )
    print singleSpanSupportLayer( )
def doubleSpanLight():
    ''' displays double span light bridge'''
    print ("Double Span, Light Roadway Bridge:")
    print 
    print doubleSpanLightRoadwayLayer( )
    print doubleSpanSupportLayer( )
    print doubleSpanSupportLayer( )
    print doubleSpanSupportLayer( )

def doubleSpanHeavy ():
    ''' displays double span Heavy bridge'''
    print ("Double Span, Heavy Roadway Bridge:")
    print 
    print doubleSpanHeavyRoadwayLayer( )
    print doubleSpanSupportLayer( )
    print doubleSpanSupportLayer( )
    print doubleSpanSupportLayer( )

def showBridgeSalesBrochure( ):
    ''' displays bridge brochure'''
    lightSingleSpan()
    
    heavySingleSpan()
   
    doubleSpanLight()

    doubleSpanHeavy()

    

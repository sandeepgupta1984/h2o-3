package hex.mojo;

import hex.Model;
import water.Key;
import water.fvec.Frame;

public class MojoDelegatingModelParameters extends Model.Parameters {
    
    public Key<Frame> _mojo_key;
    
    @Override
    public String algoName() {
        return "MojoDelegating";
    }

    @Override
    public String fullName() {
        // TODO: Set the name interactively based on the algorithm behind the MOJO
        return "Mojo Delegating Model";
    }

    @Override
    public String javaName() {
        return MojoDelegatingModel.class.getName();
    }

    @Override
    public long progressUnits() {
        return 100;
    }
}
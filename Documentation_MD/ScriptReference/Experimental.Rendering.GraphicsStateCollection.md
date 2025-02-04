[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

**Experimental** : this API is experimental and might be changed or removed in
the future.

# GraphicsStateCollection

class in UnityEngine.Experimental.Rendering

/

Inherits from:[Object](Object.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Collection of shader variants and associated graphics states.

Use graphics state collections to record shader variants and graphics states
encountered at runtime and prewarm shader variants.  
  
Each shader variant in the collection may have one or more associated graphics
states. Each permutation of a shader variant and a graphics state will result
in a single GPU representation of the shader being created by Unity.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;  
      
    public class GraphicsStateCollectionTracing : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html) graphicsStateCollection;  
      
        void Start()
        {
            graphicsStateCollection = new [GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html)();
            graphicsStateCollection.BeginTrace();
        }  
      
        void OnDestroy()
        {
            graphicsStateCollection.EndTrace();
        }
    }

### Properties

[completedWarmupCount](Experimental.Rendering.GraphicsStateCollection-
completedWarmupCount.html)| The number of shader variant permutations that
have been warmed up.  
---|---  
[graphicsDeviceType](Experimental.Rendering.GraphicsStateCollection-
graphicsDeviceType.html)| The graphics device API type the collection is
intended to be used with.  
[isTracing](Experimental.Rendering.GraphicsStateCollection-isTracing.html)|
Flag indicating if the collection is actively tracing shader variants and
graphics states.  
[isWarmedUp](Experimental.Rendering.GraphicsStateCollection-isWarmedUp.html)|
Flag indicating if the collection is warmed up.  
[qualityLevelName](Experimental.Rendering.GraphicsStateCollection-
qualityLevelName.html)| The quality level the collection is intended to be
used with.  
[runtimePlatform](Experimental.Rendering.GraphicsStateCollection-
runtimePlatform.html)| The platform that the collection is intended to be used
with.  
[totalGraphicsStateCount](Experimental.Rendering.GraphicsStateCollection-
totalGraphicsStateCount.html)| The total number of graphics states across all
shader variants in the collection.  
[variantCount](Experimental.Rendering.GraphicsStateCollection-
variantCount.html)| The number of shader variants contained in this
collection.  
[version](Experimental.Rendering.GraphicsStateCollection-version.html)| The
current version of the collection.  
  
### Constructors

[GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection-
ctor.html)| Create a GraphicsTextureCollection populated with contents of a
file, or empty.  
---|---  
  
### Public Methods

[AddGraphicsStateForVariant](Experimental.Rendering.GraphicsStateCollection.AddGraphicsStateForVariant.html)|
Adds a new graphics state associated with a shader variant.  
---|---  
[AddVariant](Experimental.Rendering.GraphicsStateCollection.AddVariant.html)|
Adds a new shader variant to the collection.  
[BeginTrace](Experimental.Rendering.GraphicsStateCollection.BeginTrace.html)|
Start tracing shader variants and graphics states encountered at runtime.  
[ClearVariants](Experimental.Rendering.GraphicsStateCollection.ClearVariants.html)|
Clears all shader variants and associated graphics states from collection.  
[ContainsVariant](Experimental.Rendering.GraphicsStateCollection.ContainsVariant.html)|
Check if variant exists in collection.  
[EndTrace](Experimental.Rendering.GraphicsStateCollection.EndTrace.html)| Stop
tracing shader variants and graphics states encountered at runtime.  
[GetGraphicsStateCountForVariant](Experimental.Rendering.GraphicsStateCollection.GetGraphicsStateCountForVariant.html)|
Get the number of graphics states associated to a shader variant.  
[GetGraphicsStatesForVariant](Experimental.Rendering.GraphicsStateCollection.GetGraphicsStatesForVariant.html)|
Populate given list with graphics states associated with input shader variant.  
[GetVariants](Experimental.Rendering.GraphicsStateCollection.GetVariants.html)|
Populate given list with shader variants contained in collection.  
[LoadFromFile](Experimental.Rendering.GraphicsStateCollection.LoadFromFile.html)|
Load the GraphicsStateCollection at the given path.  
[RemoveGraphicsStatesForVariant](Experimental.Rendering.GraphicsStateCollection.RemoveGraphicsStatesForVariant.html)|
Remove all associated graphics states from a shader variant.  
[RemoveVariant](Experimental.Rendering.GraphicsStateCollection.RemoveVariant.html)|
Remove shader variant and associated graphics states from collection.  
[SaveToFile](Experimental.Rendering.GraphicsStateCollection.SaveToFile.html)|
Save GraphicsStateCollection to disk.  
[SendToEditor](Experimental.Rendering.GraphicsStateCollection.SendToEditor.html)|
Send GraphicsStateCollection to the Editor using PlayerConnection.  
[WarmUp](Experimental.Rendering.GraphicsStateCollection.WarmUp.html)| Prewarms
all shader variants in this collection using associated graphics states.  
[WarmUpProgressively](Experimental.Rendering.GraphicsStateCollection.WarmUpProgressively.html)|
Prewarms the given number of shader variant permutations using associated
graphics states.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)


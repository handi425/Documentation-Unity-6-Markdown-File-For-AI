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

# LayerMask

struct in UnityEngine

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

Specifies Layers to use in a [Physics.Raycast](Physics.Raycast.html).

A [GameObject](GameObject.html) can use up to 32 [LayerMask](LayerMask.html)s
supported by the Editor. The first 8 of these `Layers` are specified by Unity;
the following 24 are controllable by the user.  
  
Bitmasks represent the 32 Layers and define them as `true` or `false`. Each
bitmask describes whether the `Layer` is used. As an example, bit 5 can be set
to 1 (`true`). This will allow the use of the built-in `Water` setting.  
  
`Edit->Settings->Tags and Layers` option shows the use of the 32 bitmasks.
Each `Layer` is shown with a string setting. As an example `Built-in Layer 0`
is set as `Default`; `Built-in Layer 1` is set as `TransparentFX`. New named
`Layer`s are added above bitmask layer 8. A selected `GameObject` will show
the chosen `Layer` at top right of the Inspector. The example below has `User
Layer 13` set to "Wall". This causes the assigned `GameObject` to be treated
as part of a building.  
  
In the following script example, [Physics.Raycast](Physics.Raycast.html) sends
a ray into the world. [Camera.main](Camera-main.html) can be rotated around
the y-axis and fire a ray. Three [GameObject](GameObject.html)s represent
walls that can be hit by the fired ray. Each [GameObject](GameObject.html) has
[GameObject.label](GameObject-label.html) set to the "Wall"
[layerMask](LayerMask-layerMask.html).

    
    
    using UnityEngine;  
      
    // Fire a gun at 3 walls in the scene.
    //
    // The Raycast will be aimed in the range of -45 to 45 degrees. If the [Ray](Ray.html) hits any of the
    // walls true will be returned . The three walls all have a Wall [Layer](Experimental.GraphView.GraphView.Layer.html) attached.  The left
    // and right keys, and the space key, are all used to aim and fire.
    //
    // Quad floor based at (0, -0.5, 0), rotated in x by 90 degrees, scale (8, 8, 8).
    // ZCube wall at (0, 0.5, 6), scale (3, 2, 0.5).
    // LCube wall at (-3, 0, 3), scale (0.5, 1, 4).
    // RCube wall at (3, 1.5, 3), scale (1, 4, 4).  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private float cameraRotation;  
      
        void Start()
        {
            Camera.main.transform.position = new [Vector3](Vector3.html)(0, 0.5f, 0);
            cameraRotation = 0.0f;
        }  
      
        // [Rotate](UIElements.Rotate.html) the camera based on what the user wants to look at.
        // Avoid rotating more than +/-45 degrees.
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)("left"))
            {
                cameraRotation -= 1f;
                if (cameraRotation < -45.0f)
                {
                    cameraRotation = -45.0f;
                }
            }  
      
            if ([Input.GetKey](Input.GetKey.html)("right"))
            {
                cameraRotation += 1f;
                if (cameraRotation > 45.0f)
                {
                    cameraRotation = 45.0f;
                }
            }  
      
            // [Rotate](UIElements.Rotate.html) the camera
            Camera.main.transform.localEulerAngles = new [Vector3](Vector3.html)(0.0f, cameraRotation, 0.0f);
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            [Transform](Transform.html) transform = Camera.main.transform;  
      
            if ([Input.GetKeyUp](Input.GetKeyUp.html)("space"))
            {
                // Check for a Wall.
                [LayerMask](LayerMask.html) mask = [LayerMask.GetMask](LayerMask.GetMask.html)("Wall");  
      
                // Check if a Wall is hit.
                if ([Physics.Raycast](Physics.Raycast.html)(transform.position, transform.forward, 20.0f, mask))
                {
                    [Debug.Log](Debug.Log.html)("Fired and hit a wall");
                }
            }
        }
    }
    

**Note:** [LayerMask](LayerMask.html) is a bitmask. Use
[LayerMask.GetMask](LayerMask.GetMask.html) and
[LayerMask.LayerToName](LayerMask.LayerToName.html) to generate the bitmask.

### Properties

[value](LayerMask-value.html)| Converts a layer mask value to an integer
value.  
---|---  
  
### Static Methods

[GetMask](LayerMask.GetMask.html)| Given a set of layer names as defined by
either a Builtin or a User Layer in the Tags and Layers manager, returns the
equivalent layer mask for all of them.  
---|---  
[LayerToName](LayerMask.LayerToName.html)| Given a layer number, returns the
name of the layer as defined in either a Builtin or a User Layer in the Tags
and Layers manager.  
[NameToLayer](LayerMask.NameToLayer.html)| Given a layer name, returns the
layer index as defined by either a Builtin or a User Layer in the Tags and
Layers manager.  
  
### Operators

[LayerMask](LayerMask-operator_int.html)| Implicitly converts an integer to a
LayerMask.  
---|---  
  
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


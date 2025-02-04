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

#  [Transform](Transform.html).Translate

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

## Declaration

public void Translate([Vector3](Vector3.html) translation);

## Declaration

public void Translate([Vector3](Vector3.html) translation, [Space](Space.html)
relativeTo = Space.Self);

### Description

Moves the transform in the direction and distance of `translation`.

If `relativeTo` is left out or set to [Space.Self](Space.Self.html) the
movement is applied relative to the transform's local axes. (the x, y and z
axes shown when selecting the object inside the Scene View.) If `relativeTo`
is [Space.World](Space.World.html) the movement is applied relative to the
world coordinate system.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Move the object forward along its z axis 1 unit/second.
            transform.Translate([Vector3.forward](Vector3-forward.html) * [Time.deltaTime](Time-deltaTime.html));  
      
            // Move the object upward in world space 1 unit/second.
            transform.Translate([Vector3.up](Vector3-up.html) * [Time.deltaTime](Time-deltaTime.html), [Space.World](Space.World.html));
        }
    }
    

* * *

## Declaration

public void Translate(float x, float y, float z);

## Declaration

public void Translate(float x, float y, float z, [Space](Space.html)
relativeTo = Space.Self);

### Description

Moves the transform by `x` along the x axis, `y` along the y axis, and `z`
along the z axis.

If `relativeTo` is left out or set to [Space.Self](Space.Self.html) the
movement is applied relative to the transform's local axes. (the x, y and z
axes shown when selecting the object inside the Scene View.) If `relativeTo`
is [Space.World](Space.World.html) the movement is applied relative to the
world coordinate system.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Move the object forward along its z axis 1 unit/second.
            transform.Translate(0, 0, [Time.deltaTime](Time-deltaTime.html));  
      
            // Move the object upward in world space 1 unit/second.
            transform.Translate(0, [Time.deltaTime](Time-deltaTime.html), 0, [Space.World](Space.World.html));
        }
    }
    

* * *

## Declaration

public void Translate([Vector3](Vector3.html) translation,
[Transform](Transform.html) relativeTo);

### Description

Moves the transform in the direction and distance of `translation`.

The movement is applied relative to `relativeTo`'s local coordinate system. If
`relativeTo` is null, the movement is applied relative to the world coordinate
system.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Move the object to the right relative to the camera 1 unit/second.
            transform.Translate([Vector3.right](Vector3-right.html) * [Time.deltaTime](Time-deltaTime.html), Camera.main.transform);
        }
    }
    

* * *

## Declaration

public void Translate(float x, float y, float z, [Transform](Transform.html)
relativeTo);

### Description

Moves the transform by `x` along the x axis, `y` along the y axis, and `z`
along the z axis.

The movement is applied relative to `relativeTo`'s local coordinate system. If
`relativeTo` is null, the movement is applied relative to the world coordinate
system.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Move the object to the right relative to the camera 1 unit/second.
            transform.Translate([Time.deltaTime](Time-deltaTime.html), 0, 0, Camera.main.transform);
        }
    }
    

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


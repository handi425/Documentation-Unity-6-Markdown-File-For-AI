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

#  [Vector3](Vector3.html).Reflect

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

## Declaration

public static [Vector3](Vector3.html) Reflect([Vector3](Vector3.html)
inDirection, [Vector3](Vector3.html) inNormal);

### Parameters

inDirection | The direction vector towards the plane.  
---|---  
inNormal | The normal vector that defines the plane.  
  
### Description

Reflects a vector off the plane defined by a normal.

This method calculates the reflection vector using the following formula: v =
inDirection - 2 * inNormal * dot(inDirection inNormal). The `inNormal` vector
defines a plane. A plane's normal is the vector that is perpendicular to its
surface. The `inDirection` vector is treated as a directional arrow coming
into the plane. The returned value is a vector of equal magnitude to
`inDirection` but with its direction reflected.  
  
![](../StaticFiles/ScriptRefImages/Vec3ReflectDiagram.png)  
_Reflection of a vector off a plane._

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) originalObject;
        public [Transform](Transform.html) reflectedObject;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Makes the reflected object appear opposite of the original object,
            // mirrored along the z-axis of the world
            reflectedObject.position = [Vector3.Reflect](Vector3.Reflect.html)(originalObject.position, [Vector3.right](Vector3-right.html));
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


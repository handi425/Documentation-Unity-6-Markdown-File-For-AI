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

#  [Matrix4x4](Matrix4x4.html).Rotate

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

public static [Matrix4x4](Matrix4x4.html) Rotate([Quaternion](Quaternion.html)
q);

### Description

Creates a rotation matrix.

    
    
    // [Translate](UIElements.Translate.html), rotate and scale a mesh. Try varying
        // the parameters in the inspector while running
        // to see the effect they have.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {
        public [Vector3](Vector3.html) eulerAngles;
        private [MeshFilter](MeshFilter.html) mf;
        private [Vector3](Vector3.html)[] origVerts;
        private [Vector3](Vector3.html)[] newVerts;  
      
        void Start() {
            mf = GetComponent<[MeshFilter](MeshFilter.html)>();
            origVerts = mf.mesh.vertices;
            newVerts = new [Vector3](Vector3.html)[origVerts.Length];
        }  
      
        void [Update](PlayerLoop.Update.html)() {
            [Quaternion](Quaternion.html) rotation = [Quaternion.Euler](Quaternion.Euler.html)(eulerAngles.x, eulerAngles.y, eulerAngles.z);
            [Matrix4x4](Matrix4x4.html) m = [Matrix4x4.Rotate](Matrix4x4.Rotate.html)(rotation);
            int i = 0;
            while (i < origVerts.Length) {
                newVerts[i] = m.MultiplyPoint3x4(origVerts[i]);
                i++;
            }
            mf.mesh.vertices = newVerts;
        }
    }
    

Additional resources: [TRS](Matrix4x4.TRS.html),
[Scale](Matrix4x4.Scale.html), [Translate](Matrix4x4.Translate.html),
[SetTRS](Matrix4x4.SetTRS.html) functions.

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


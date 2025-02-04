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

#  [Quaternion](Quaternion.html).w

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

[Switch to Manual](../Manual/class-Quaternion.html "Go to Quaternion Component
in the Manual")

public float w;

### Description

W component of the Quaternion. Do not directly modify quaternions.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [Quaternion](Quaternion.html)-w script example
    // Create a Sphere and apply a texture to help the orientation be recognised.
    // At each second the sphere is rotated and the quaternion is displayed.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private float timeDelay = 0.0f;
        private [Quaternion](Quaternion.html) q;
        private string label = "";  
      
        void Awake()
        {
            // Add a line that passes through the y axis of the sphere and make
            // the line as a child.
            [GameObject](GameObject.html) line = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            line.transform.localScale = new [Vector3](Vector3.html)(0.05f, 1.5f, 0.05f);
            line.transform.parent = gameObject.transform;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (timeDelay > 1.0f)
            {
                [Vector3](Vector3.html) v;  
      
                // generate a random euler angle
                v.x = [Random.Range](Random.Range.html)(0.0f, 360.0f);
                v.y = [Random.Range](Random.Range.html)(0.0f, 360.0f);
                v.z = [Random.Range](Random.Range.html)(0.0f, 360.0f);  
      
                // convert the euler into a quaternion
                q = [Quaternion.Euler](Quaternion.Euler.html)(v);  
      
                // and apply it to the sphere
                transform.rotation = q;  
      
                // generate a string
                label = q.ToString("f3");  
      
                // and start another 1 second delay
                timeDelay = 0.0f;
            }
            timeDelay += [Time.deltaTime](Time-deltaTime.html);
        }  
      
        // display the quaternion as a string
        void OnGUI()
        {
            GUI.skin.label.fixedHeight = 40;
            GUI.skin.label.fontSize = 24;
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 10, 400, 30), label);
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


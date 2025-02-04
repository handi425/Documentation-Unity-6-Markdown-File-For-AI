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

#  [Handles](Handles.html).color

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

public static [Color](Color.html) color;

### Description

Sets the color of handles. Color is a persistent state and affects any handles
drawn after it is set. Use [DrawingScope](Handles.DrawingScope.html) to set
the color for a block of handles without affecting the color of other handles.

![](../StaticFiles/ScriptRefImages/SliderHandle.png)  
_White cone that points to 0,0,0._

    
    
    // Name this script "SliderHandleEditor"
    using UnityEngine;
    using System.Collections;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(SliderHandle))]
    public class SliderHandleEditor : [Editor](Editor.html)
    {
        // Simple script that creates a Slide Handle that
        // allows you to drag a 'look at' point along the X axis  
      
        void OnSceneGUI()
        {
            SliderHandle t = (target as SliderHandle);  
      
            // Set the colour of the next handle to be drawn:
            [Handles.color](Handles-color.html) = [Color.magenta](Color-magenta.html);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Vector3](Vector3.html) lookTarget = [Handles.Slider](Handles.Slider.html)(t.lookTarget, new [Vector3](Vector3.html)(1, 0, 0), 2, [Handles.ConeHandleCap](Handles.ConeHandleCap.html), 0.1f);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Changed [Slider](UIElements.Slider.html) Look [Target](GraphicsBuffer.Target.html)");
                t.lookTarget = lookTarget;
                t.Update();
            }
        }
    }
    

And the script attached to this GameObject:

    
    
    // Name this script "SliderHandle"
    using UnityEngine;
    using System.Collections;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class SliderHandle : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) lookTarget = new [Vector3](Vector3.html)(0, 0, 0);  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            transform.LookAt(lookTarget);
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


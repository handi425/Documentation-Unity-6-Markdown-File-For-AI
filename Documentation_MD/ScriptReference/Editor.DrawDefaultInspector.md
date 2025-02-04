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

#  [Editor](Editor.html).DrawDefaultInspector

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

public bool DrawDefaultInspector();

### Returns

**bool** Returns true if any GUI controls in the default Inspector changed the
value of the input data, otherwise returns false.

### Description

Draws the built-in Inspector.

Call this method, within the OnInspectorGUI method, to automatically draw the
Inspector. This is useful if you want to add a few buttons without having to
redo the entire Inspector. Additional resources:
[OnInspectorGUI](Editor.OnInspectorGUI.html).

    
    
    // This example shows a custom inspector for an
    // object "MyPlayer", which has a variable speed.
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class MyPlayer : [MonoBehaviour](MonoBehaviour.html)
    {
        // Hide this field so that it is not shown twice when drawing the default Inspector.
        [[HideInInspector](HideInInspector.html)]
        public float speed;  
      
        public int gear;
    }  
      
    [[CustomEditor](CustomEditor.html)(typeof(MyPlayer))]
    public class Example : [Editor](Editor.html)
    {
        public override void OnInspectorGUI()
        {
            MyPlayer targetPlayer = (MyPlayer)target;
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html) ("Some help", "Some other text");  
      
            targetPlayer.speed = [EditorGUILayout.Slider](EditorGUILayout.Slider.html) ("Speed", targetPlayer.speed, 0, 100);  
      
            // Show default inspector property editor
            if(DrawDefaultInspector())
                [Debug.Log](Debug.Log.html)("Gear was changed!");
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


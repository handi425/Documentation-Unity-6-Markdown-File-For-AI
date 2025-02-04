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

#  [EditorGUIUtility](EditorGUIUtility.html).ObjectContent

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

public static [GUIContent](GUIContent.html)
ObjectContent([Object](Object.html) obj, Type type);

### Description

Return a GUIContent object with the name and icon of an Object.

If the object is null, the icon will be picked according to type.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIUtilityObjectContent.png)  
_Object Content usage._

    
    
    // Simple [Editor](Editor.html) Script that shows the icons of [Transform](Transform.html),
    // rigidbody and [GameObject](GameObject.html) in 3 buttons.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ObjectContentExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/ObjectContent usage")]
        static void Init()
        {
            ObjectContentExample window = (ObjectContentExample)GetWindow(typeof(ObjectContentExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.PrefixLabel](EditorGUILayout.PrefixLabel.html)("Select a type:");
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            if ([GUILayout.Button](GUILayout.Button.html)([EditorGUIUtility.ObjectContent](EditorGUIUtility.ObjectContent.html)(null, typeof([Transform](Transform.html))).image))
                DoSomething("[Transform](Transform.html)");
            if ([GUILayout.Button](GUILayout.Button.html)([EditorGUIUtility.ObjectContent](EditorGUIUtility.ObjectContent.html)(null, typeof([Rigidbody](Rigidbody.html))).image))
                DoSomething("RigidBody");
            if ([GUILayout.Button](GUILayout.Button.html)([EditorGUIUtility.ObjectContent](EditorGUIUtility.ObjectContent.html)(null, typeof([GameObject](GameObject.html))).image))
                DoSomething("[GameObject](GameObject.html)");
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Close"))
                this.Close();
        }  
      
        private void DoSomething(string obj)
        {
            [Debug.Log](Debug.Log.html)("Hello there " + obj + "!");
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


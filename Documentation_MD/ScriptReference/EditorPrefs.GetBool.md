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

#  [EditorPrefs](EditorPrefs.html).GetBool

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

public static bool GetBool(string key);

## Declaration

public static bool GetBool(string key, bool defaultValue = false);

### Description

Returns the value corresponding to `key` in the preference file if it exists.

If it doesn't exist, it will return `defaultValue`.  
  
![](../StaticFiles/ScriptRefImages/EditorPrefsBool.png)  
_Round rotations/positions and remember the active option._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorPrefsBoolExample : [EditorWindow](EditorWindow.html)
    {
        bool showRoundPosition = true;
        bool showRoundRotation = true;  
      
        [[MenuItem](MenuItem.html)("Examples/Round positions-rotations")]
        static void Init()
        {
            EditorPrefsBoolExample window = (EditorPrefsBoolExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(EditorPrefsBoolExample), true, "My Empty Window");
            window.Show();
        }  
      
        void OnGUI()
        {
            showRoundPosition = [EditorGUILayout.BeginToggleGroup](EditorGUILayout.BeginToggleGroup.html)("Round [Position](UIElements.Position.html)", showRoundPosition);
            if ([GUILayout.Button](GUILayout.Button.html)("Round [Position](UIElements.Position.html)!"))
                DoRoundPosition();
            [EditorGUILayout.EndToggleGroup](EditorGUILayout.EndToggleGroup.html)();
            showRoundRotation = [EditorGUILayout.BeginToggleGroup](EditorGUILayout.BeginToggleGroup.html)("Round Rotation", showRoundRotation);
            if ([GUILayout.Button](GUILayout.Button.html)("Round Rotation!"))
                DoRoundRotation();
            [EditorGUILayout.EndToggleGroup](EditorGUILayout.EndToggleGroup.html)();
        }  
      
        void DoRoundPosition()
        {
            foreach ([Transform](Transform.html) t in [Selection.transforms](Selection-transforms.html))
                t.localPosition = new [Vector3](Vector3.html)([Mathf.Round](Mathf.Round.html)(t.localPosition.x),
                    [Mathf.Round](Mathf.Round.html)(t.localPosition.z),
                    [Mathf.Round](Mathf.Round.html)(t.localPosition.y));
        }  
      
        void DoRoundRotation()
        {
            foreach ([Transform](Transform.html) t in [Selection.transforms](Selection-transforms.html))
                t.rotation = [Quaternion.Euler](Quaternion.Euler.html)(
                    new [Vector3](Vector3.html)([Mathf.Round](Mathf.Round.html)(t.eulerAngles.x / 45f) * 45f,
                        [Mathf.Round](Mathf.Round.html)(t.eulerAngles.y / 45f) * 45f,
                        [Mathf.Round](Mathf.Round.html)(t.eulerAngles.z / 45f) * 45f));
        }  
      
        void OnFocus()
        {
            if ([EditorPrefs.HasKey](EditorPrefs.HasKey.html)("ShowRoundPosition"))
                showRoundPosition = [EditorPrefs.GetBool](EditorPrefs.GetBool.html)("ShowRoundPosition");
            if ([EditorPrefs.HasKey](EditorPrefs.HasKey.html)("ShowRoundRotation"))
                showRoundPosition = [EditorPrefs.GetBool](EditorPrefs.GetBool.html)("ShowRoundRotation");
        }  
      
        void OnLostFocus()
        {
            [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("ShowRoundPosition", showRoundPosition);
            [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("ShowRoundRotation", showRoundRotation);
        }  
      
        void OnDestroy()
        {
            [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("ShowRoundPosition", showRoundPosition);
            [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("ShowRoundRotation", showRoundRotation);
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


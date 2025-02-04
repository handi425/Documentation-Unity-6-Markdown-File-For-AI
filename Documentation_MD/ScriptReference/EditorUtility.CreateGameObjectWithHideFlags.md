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

#  [EditorUtility](EditorUtility.html).CreateGameObjectWithHideFlags

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

public static [GameObject](GameObject.html)
CreateGameObjectWithHideFlags(string name, [HideFlags](HideFlags.html) flags,
params Type[] components);

### Description

Creates a game object with [HideFlags](HideFlags.html) and specified
components.

This is very similar to creating a [GameObject](GameObject.html) the usual
way, except it sets the specified [HideFlags](HideFlags.html) immediately.  
  
![](../StaticFiles/ScriptRefImages/EditorUtility
CreateGameObjectWithHideFlags.png) _Editor Window that shows how does the
example looks._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CreateGOHideFlagsExample : [EditorWindow](EditorWindow.html)
    {
        string objName = "[GameObject](GameObject.html)";
        int instanceID = 0;
        bool create = true;
        [GameObject](GameObject.html) go = null;
        bool hideHierarchy = false;  
      
        [[MenuItem](MenuItem.html)("Example/[GameObject](GameObject.html) [Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)")]
        static void Init()
        {
            // Get existing open window or if none, make a new one:
            CreateGOHideFlagsExample window = (CreateGOHideFlagsExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(CreateGOHideFlagsExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            create = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Create a GO:", create);
            [GUI.enabled](GUI-enabled.html) = create;  
      
            objName = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("[GameObject](GameObject.html) Name:", objName);
            if ([GUILayout.Button](GUILayout.Button.html)("Create"))
            {
                [GameObject](GameObject.html) created = [EditorUtility.CreateGameObjectWithHideFlags](EditorUtility.CreateGameObjectWithHideFlags.html)(objName,
                    hideHierarchy ? [HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html) : 0);  
      
                instanceID = created.GetInstanceID();
                [Debug.Log](Debug.Log.html)("Created [GameObject](GameObject.html) ID: " + instanceID);
            }  
      
            [GUI.enabled](GUI-enabled.html) = !create;  
      
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();  
      
            instanceID = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Instance ID:", instanceID);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Search & [Update](PlayerLoop.Update.html) flags"))
            {
                go = null;
                go = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(instanceID) as [GameObject](GameObject.html);
                if (go)
                    go.hideFlags = hideHierarchy ? [HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html) : 0;
            }  
      
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            if (!go)
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Object: ", (go == null) ? "No object was found" : go.name);  
      
            [GUI.enabled](GUI-enabled.html) = true;
            hideHierarchy = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("HideInHierarchy", hideHierarchy);
        }  
      
        void OnInspectorUpdate()
        {
            Repaint();
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


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

#  [EditorUtility](EditorUtility.html).InstanceIDToObject

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

public static Object InstanceIDToObject(int instanceID);

### Description

Translates an instance ID to a reference to an object.

If the object is not loaded from disk, loads it from disk.  
  
![](../StaticFiles/ScriptRefImages/EditorUtilityInstanceIDToObject.png)  
_Editor Window to enter the instance ID and print the name of the object._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class InstanceIDToObjectExample : [EditorWindow](EditorWindow.html)
    {
        static int id;  
      
        [[MenuItem](MenuItem.html)("Example/ID To Name")]
        static void Init()
        {
            // Get existing open window or if none, make a new one:
            InstanceIDToObjectExample window = (InstanceIDToObjectExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(InstanceIDToObjectExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            id = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Instance ID:", id);
            if ([GUILayout.Button](GUILayout.Button.html)("Find Name"))
            {
                Object obj = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(id);
                if (!obj)
                    [Debug.LogError](Debug.LogError.html)("No object could be found with instance id: " + id);
                else
                    [Debug.Log](Debug.Log.html)("Object's name: " + obj.name);
            }
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


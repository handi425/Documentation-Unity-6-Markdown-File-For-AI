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

#  [Editor](Editor.html).CreateEditor

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

public static [Editor](Editor.html) CreateEditor([Object](Object.html)
targetObject, Type editorType = null);

## Declaration

public static [Editor](Editor.html) CreateEditor(Object[] targetObjects, Type
editorType = null);

### Parameters

objects | All objects must be of the same type.  
---|---  
  
### Description

Make a custom editor for `targetObject` or `targetObjects`.

By default, an appropriate editor with a matching CustomEditor attribute is
created. If an editorType is specified, an editor of that type is created
instead. Use this if you have created multiple custom editors, and each editor
shows different properties of the object. Returns NULL if `objects` are of
different types or if no approprate editor was found. Editors created using
this function have to be destroyed explicitly, using either
[Object.Destroy](Object.Destroy.html) or
[Object.DestroyImmediate](Object.DestroyImmediate.html).  
  
Consider a script WaypointPathEditor for editing the Transforms of a wayPoint
array.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    
    [[CustomEditor](CustomEditor.html)(typeof(WaypointPath))]
    public class WaypointPathEditor : [Editor](Editor.html)
    {
        [Editor](Editor.html) currentTransformEditor;
        [Transform](Transform.html) selectedTransform;
        string[] optionsList;
        int index = 0;
        WaypointPath myWayPath;  
      
        void GetWaypoints()
        {
            myWayPath = target as WaypointPath;  
      
            if (myWayPath.wayPointArray != null)
            {
                optionsList = new string[myWayPath.wayPointArray.Length];  
      
                for (int i = 0; i < optionsList.Length; i++)
                {
                    [Transform](Transform.html) wayPoint = myWayPath.wayPointArray[i];  
      
                    if (wayPoint != null)
                        optionsList[i] = wayPoint.name;
                    else
                        optionsList[i] = $"Empty waypoint {(i + 1)}";
                }
            }
        }  
      
        public override void OnInspectorGUI()
        {
            GetWaypoints ();
            DrawDefaultInspector ();
            [EditorGUILayout.Space](EditorGUILayout.Space.html) ();
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html) ();  
      
            if (optionsList != null)
                index = [EditorGUILayout.Popup](EditorGUILayout.Popup.html) ("Select Waypoint", index, optionsList);  
      
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Editor](Editor.html) tmpEditor = null;  
      
                if (index < myWayPath.wayPointArray.Length)
                {
                    selectedTransform = myWayPath.wayPointArray[index];  
      
                    //Creates an [Editor](Editor.html) for selected [Component](Component.html) from a Popup
                    tmpEditor = [Editor.CreateEditor](Editor.CreateEditor.html)(selectedTransform);
                } else {
                    selectedTransform = null;
                }  
      
                // If there isn't a [Transform](Transform.html) currently selected then destroy the existing editor
                if (currentTransformEditor != null)
                {
                    DestroyImmediate (currentTransformEditor);
                }  
      
                currentTransformEditor = tmpEditor;
            }  
      
            // Shows the created [Editor](Editor.html) beneath [CustomEditor](CustomEditor.html)
            if (currentTransformEditor != null && selectedTransform != null)
            {
                currentTransformEditor.OnInspectorGUI ();
            }
        }
    }
    

The script attached to a waypath GameObject:

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Note: this is not an editor script.
    public class WaypointPath : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html)[] wayPointArray;
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


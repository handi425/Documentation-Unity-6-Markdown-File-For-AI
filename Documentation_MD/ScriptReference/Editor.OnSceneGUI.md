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

#  [Editor](Editor.html).OnSceneGUI()

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

### Description

Enables the Editor to handle an event in the Scene view.

In the [OnSceneGUI](Editor.OnSceneGUI.html) you can, for example, edit meshes,
paint terrain, or have advanced gizmos. Refer to the [Handles](Handles.html)
class for methods related to drawing interactable visuals in the
[SceneView](SceneView.html).  
  
If you want to draw elements in the Scene view, for instance by using
`Graphics.DrawMeshNow`, only do so during
[EventType.Repaint](EventType.Repaint.html).  
  
In the following two scripts, [OnSceneGUI](Editor.OnSceneGUI.html) is used to
draw lines between GameObjects. The first script shows how
[OnSceneGUI](Editor.OnSceneGUI.html) is used. In this script, a GameObject is
used as a parent. The script obtains the position of the parent and then draws
lines from that position to GameObjects stored in an array. The script uses
[Handles.DrawLine](Handles.DrawLine.html) to draw lines. The documentation for
[Handles.DrawLine](Handles.DrawLine.html) has a very similar example.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)( typeof( DrawLine ) )]
    public class DrawLineEditor : [Editor](Editor.html)
    {
        // Draw lines between a chosen [GameObject](GameObject.html)
        // and a selection of added GameObjects  
      
        void OnSceneGUI()
        {
            // Get the chosen [GameObject](GameObject.html)
            DrawLine t = target as DrawLine;  
      
            if( t == null || t.GameObjects == null )
                return;  
      
            // Grab the center of the parent
            [Vector3](Vector3.html) center = t.transform.position;  
      
            // Iterate over [GameObject](GameObject.html) added to the array...
            for( int i = 0; i < t.GameObjects.Length; i++ )
            {
                // ... and draw a line between them
                if( t.GameObjects[i] != null )
                    [Handles.DrawLine](Handles.DrawLine.html)( center, t.GameObjects[i].transform.position );
            }
        }
    }
    

This script stores the array of GameObjects which have a line drawn to them.
This regular script is attached to a GameObject which is considered to be the
starting point for all lines.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class DrawLine : [MonoBehaviour](MonoBehaviour.html)
    {
        // an array of game objects which will have a
        // line drawn to in the [Scene](SceneManagement.Scene.html) editor
        public [GameObject](GameObject.html)[] GameObjects;
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


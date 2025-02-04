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

#  [Handles](Handles.html).DrawPolyLine

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

public static void DrawPolyLine(params Vector3[] points);

### Description

Draw a line going through the list of `points`.

**Note:** Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)
where you might want to have constant screen-sized handles.  
  
![](../StaticFiles/ScriptRefImages/DrawPolyLine.png)  
_PolyLine that connects all the objects in the Scene View._

    
    
    // Draw lines between selected GameObjects.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    [[CustomEditor](CustomEditor.html)(typeof(DrawPolyLineExample))]
    public class PolyLineDraw : [Editor](Editor.html)
    {
        private [Vector3](Vector3.html)[] positions;  
      
        void OnSceneGUI()
        {
            DrawPolyLineExample connectedObjects = target as DrawPolyLineExample;
            if (connectedObjects.objs == null)
            {
                return;
            }  
      
            if (connectedObjects.objs.Length > 0)
            {
                positions = new [Vector3](Vector3.html)[connectedObjects.objs.Length];
            }  
      
            for (var i = 0; i < connectedObjects.objs.Length; i++)
            {
                if (connectedObjects.objs[i])
                {
                    positions[i] = connectedObjects.objs[i].transform.position;
                }
                else
                {
                    positions[i] = [Vector3.zero](Vector3-zero.html);
                }
            }  
      
            [Handles.DrawPolyLine](Handles.DrawPolyLine.html)(positions);
        }
    }
    

And the script attached to this handle:

    
    
    using UnityEngine;  
      
    public class DrawPolyLineExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html)[] objs;
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


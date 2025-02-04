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

#  [TrailRenderer](TrailRenderer.html).AddPositions

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

[Switch to Manual](../Manual/class-TrailRenderer.html "Go to TrailRenderer
Component in the Manual")

## Declaration

public void AddPositions(Vector3[] positions);

## Declaration

public void AddPositions(out NativeArray<Vector3> positions);

## Declaration

public void AddPositions(out NativeSlice<Vector3> positions);

### Parameters

positions | The positions to add to the trail.  
---|---  
  
### Description

Add an array of positions to the trail.

All points inside a TrailRenderer store a timestamp when they are born. This,
together with the [TrailRenderer.time](time.html) property, is used to
determine when they will be removed. For trails to disappear smoothly, each
position must have a unique, increasing timestamp. When positions are supplied
from script and the current time is identical for multiple points, position
timestamps are adjusted to interpolate smoothly between the timestamp of the
newest existing point in the trail and the current time.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;  
      
    [[RequireComponent](RequireComponent.html)(typeof([TrailRenderer](TrailRenderer.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public int numExtraPositions = 0;
        public float speed = 20.0f;
        public float radius = 4.0f;  
      
        private [TrailRenderer](TrailRenderer.html) tr;  
      
        void Start()
        {
            tr = GetComponent<[TrailRenderer](TrailRenderer.html)>();
            tr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
            tr.time = 0.2f;
            tr.widthMultiplier = 0.3f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float time = [Time.time](Time-time.html);
            tr.transform.position = CalculatePosition(time);  
      
            if (numExtraPositions > 0)
            {
                float prevTime = time - [Time.deltaTime](Time-deltaTime.html);
                List<[Vector3](Vector3.html)> extraPositions = new List<[Vector3](Vector3.html)>(numExtraPositions);  
      
                for (int i = 0; i < numExtraPositions; i++)
                {
                    float percentage = (float)(i + 1) / (numExtraPositions + 1);
                    float blendedTime = [Mathf.LerpUnclamped](Mathf.LerpUnclamped.html)(prevTime, time, percentage);
                    extraPositions.Add(CalculatePosition(blendedTime));
                }  
      
                tr.AddPositions(extraPositions.ToArray());
            }
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 20, 200, 30), "Extra Positions");
            numExtraPositions = (int)[GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, 25, 200, 30), (float)numExtraPositions, 0, 5);
        }  
      
        private [Vector3](Vector3.html) CalculatePosition(float time)
        {
            return new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)(time * speed) * radius, [Mathf.Cos](Mathf.Cos.html)(time * speed) * radius, 0.0f);
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


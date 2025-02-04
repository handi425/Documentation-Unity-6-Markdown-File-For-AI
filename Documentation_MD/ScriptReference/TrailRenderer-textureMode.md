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

#  [TrailRenderer](TrailRenderer.html).textureMode

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

public [LineTextureMode](LineTextureMode.html) textureMode;

### Description

Choose whether the U coordinate of the trail texture is tiled or stretched.

Stretching maps the texture along the trail with no repeats. Tiling maps the
texture along the trail with repeats every world unit. To change the repeat
rate, use [TrailRenderer.textureScale](TrailRenderer-textureScale.html) or
[Material.SetTextureScale](Material.SetTextureScale.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([TrailRenderer](TrailRenderer.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [LineTextureMode](LineTextureMode.html) textureMode = [LineTextureMode.Stretch](LineTextureMode.Stretch.html);
        public float textureScale = 1.0f;
        private [TrailRenderer](TrailRenderer.html) tr;  
      
        void Start()
        {
            tr = GetComponent<[TrailRenderer](TrailRenderer.html)>();
            tr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            tr.textureMode = textureMode;
            tr.textureScale = new [Vector2](Vector2.html)(textureScale, 1.0f);
            tr.transform.position = new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html) * 1.51f) * 7.0f, [Mathf.Cos](Mathf.Cos.html)([Time.time](Time-time.html) * 1.27f) * 4.0f, 0.0f);
        }  
      
        void OnGUI()
        {
            textureMode = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 25, 200, 30), textureMode == [LineTextureMode.Tile](LineTextureMode.Tile.html), "Tiled") ? [LineTextureMode.Tile](LineTextureMode.Tile.html) : [LineTextureMode.Stretch](LineTextureMode.Stretch.html);  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 60, 200, 30), "[Tile](WSA.Tile.html) Amount");
            textureScale = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(125, 65, 200, 30), textureScale, 0.1f, 4.0f);
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


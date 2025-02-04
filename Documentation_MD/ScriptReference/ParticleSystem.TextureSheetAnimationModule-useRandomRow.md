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

**Method group is Obsolete**  

#
[ParticleSystem.TextureSheetAnimationModule](ParticleSystem.TextureSheetAnimationModule.html).useRandomRow

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

**Obsolete** useRandomRow property is deprecated. Use rowMode instead. public
bool useRandomRow;

### Description

Use a random row of the Texture sheet for each particle emitted.

    
    
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool useRandomRow = true;
        public int row = 0;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startLifetimeMultiplier = 2.0f;  
      
            var tex = ps.textureSheetAnimation;
            tex.enabled = true;
            tex.numTilesX = 4;
            tex.numTilesY = 2;
            tex.animation = [ParticleSystemAnimationType.SingleRow](ParticleSystemAnimationType.SingleRow.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var tex = ps.textureSheetAnimation;
            tex.useRandomRow = useRandomRow;
            tex.rowIndex = row;
        }  
      
        void OnGUI()
        {
            useRandomRow = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 20, 100, 30), useRandomRow, "Use [Random](Random.html) Row");  
      
            if (useRandomRow == false)
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 60, 100, 30), "Row Index");
                row = (int)[GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(125, 65, 100, 30), (float)row, 0.0f, 1.0f);
            }
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


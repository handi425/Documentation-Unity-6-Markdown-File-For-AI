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

# FilterMode

enumeration

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

Filtering mode for textures. Corresponds to the settings in a [texture
inspector](../Manual/Textures.html).

Additional resources: [Texture.filterMode](Texture-filterMode.html), [texture
assets](../Manual/Textures.html).

    
    
    //This script changes the filter mode of your [Texture](Texture.html) you attach when you press the space key in Play [Mode](Scripting.GarbageCollector.Mode.html). It switches between Point, Bilinear and Trilinear filter modes.
    //Attach this script to a [GameObject](GameObject.html)
    //Click on the [GameObject](GameObject.html) and attach a [Texture](Texture.html) to the My [Texture](Texture.html) field in the Inspector.
    //Apply the [Texture](Texture.html) to GameObjects (click and drag the [Texture](Texture.html) onto a [GameObject](GameObject.html) in [Editor](Editor.html) mode) in your [Scene](SceneManagement.Scene.html) to see it change modes in-game.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Remember to assign a [Texture](Texture.html) in the Inspector window to ensure this works
        public [Texture](Texture.html) m_MyTexture;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space key to switch between Filter Modes
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //[Switch](PlayerSettings.Switch.html) the [Texture](Texture.html)'s Filter [Mode](Scripting.GarbageCollector.Mode.html)
                m_MyTexture.filterMode = SwitchFilterModes();
                //Output the current Filter [Mode](Scripting.GarbageCollector.Mode.html) to the console
                [Debug.Log](Debug.Log.html)("Filter mode : " + m_MyTexture.filterMode);
            }
        }  
      
        //[Switch](PlayerSettings.Switch.html) between Filter Modes when the user clicks the [Button](UIElements.Button.html)
        [FilterMode](FilterMode.html) SwitchFilterModes()
        {
            //[Switch](PlayerSettings.Switch.html) the Filter [Mode](Scripting.GarbageCollector.Mode.html) of the [Texture](Texture.html) when user clicks the [Button](UIElements.Button.html)
            switch (m_MyTexture.filterMode)
            {
                //If the [FilterMode](FilterMode.html) is currently Bilinear, switch it to Point on the [Button](UIElements.Button.html) click
                case [FilterMode.Bilinear](FilterMode.Bilinear.html):
                    m_MyTexture.filterMode = [FilterMode.Point](FilterMode.Point.html);
                    break;  
      
                //If the [FilterMode](FilterMode.html) is currently Point, switch it to Trilinear on the [Button](UIElements.Button.html) click
                case [FilterMode.Point](FilterMode.Point.html):
                    m_MyTexture.filterMode = [FilterMode.Trilinear](FilterMode.Trilinear.html);
                    break;  
      
                //If the [FilterMode](FilterMode.html) is currently Trilinear, switch it to Bilinear on the [Button](UIElements.Button.html) click
                case [FilterMode.Trilinear](FilterMode.Trilinear.html):
                    m_MyTexture.filterMode = [FilterMode.Bilinear](FilterMode.Bilinear.html);
                    break;
            }
            //Return the new [Texture](Texture.html) [FilterMode](FilterMode.html)
            return m_MyTexture.filterMode;
        }
    }
    

### Properties

[Point](FilterMode.Point.html)| Point filtering - texture pixels become blocky
up close.  
---|---  
[Bilinear](FilterMode.Bilinear.html)| Bilinear filtering - texture samples are
averaged.  
[Trilinear](FilterMode.Trilinear.html)| Trilinear filtering - texture samples
are averaged and also blended between mipmap levels.  
  
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


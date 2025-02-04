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

#  [SpriteAtlasManager](U2D.SpriteAtlasManager.html).atlasRequested

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

Trigger when any [Sprite](Sprite.html) was bound to
[SpriteAtlas](U2D.SpriteAtlas.html) but couldn't locate the atlas asset during
runtime.

This usually means the sprite was packed to an atlas which is not included in
build  
  
This callback does not expect an immediate response from the user. Instead, it
passes on a System.Action. The user can load the atlas object later and use
this System.Action to pass back the loaded atlas.

    
    
    using UnityEngine;
    using UnityEngine.U2D;  
      
    public class AtlasLoader : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnEnable()
        {
            [SpriteAtlasManager.atlasRequested](U2D.SpriteAtlasManager-atlasRequested.html) += RequestAtlas;
        }  
      
        void OnDisable()
        {
            [SpriteAtlasManager.atlasRequested](U2D.SpriteAtlasManager-atlasRequested.html) -= RequestAtlas;
        }  
      
        void RequestAtlas(string tag, System.Action<[SpriteAtlas](U2D.SpriteAtlas.html)> callback)
        {
            var sa = [Resources.Load](Resources.Load.html)<[SpriteAtlas](U2D.SpriteAtlas.html)>(tag);
            callback(sa);
        }
    }
    

Additional resources: U2D.SpriteAtlasManager.RequestAtlasCallback.

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


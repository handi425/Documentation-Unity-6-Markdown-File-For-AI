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

#  [Texture](Texture.html).updateCount

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

public uint updateCount;

### Description

This counter is incremented when the Texture is updated.

Note: If you perform an update from the GPU side, you should increment the
counter yourself. (For instance, when blitting into a
[RenderTexture](RenderTexture.html)). (see
[IncrementUpdateCount](Texture.IncrementUpdateCount.html)).

    
    
    using UnityEngine;
    using System.Collections.Generic;  
      
    public class MyTextureCache
    {
        struct TextureCacheMeta
        {
            internal int index;
            internal uint updateCount;
        }  
      
        Dictionary<[Texture](Texture.html), TextureCacheMeta> m_TextureMetas = new Dictionary<[Texture](Texture.html), TextureCacheMeta>();
        [RenderTexture](RenderTexture.html) m_Cache;  
      
        public [Texture](Texture.html) cache { get { return m_Cache; } }  
      
        public int CacheTexture([Texture](Texture.html) [Texture](Texture.html))
        {
            var index = -1;
            TextureCacheMeta meta;
            if (m_TextureMetas.TryGetValue([Texture](Texture.html), out meta))
            {
                if (meta.updateCount != [Texture.updateCount](Texture-updateCount.html))
                {
                    // [Texture](Texture.html) has changed since last caching
                    // So blit again into the cache [Texture](Texture.html)
                    BlitTextureAt(meta.index, [Texture](Texture.html));
                    meta.updateCount = [Texture.updateCount](Texture-updateCount.html);
                    m_TextureMetas[[Texture](Texture.html)] = meta;
                }
            }
            else
            {
                index = GetNextIndex();
                if (index < 0)
                {
                    [Debug.LogError](Debug.LogError.html)("Invalid index");
                    return -1;
                }  
      
                m_TextureMetas[[Texture](Texture.html)] = new TextureCacheMeta
                {
                    index = index,
                    updateCount = [Texture.updateCount](Texture-updateCount.html)
                };
            }
            return index;
        }  
      
        void BlitTextureAt(int index, [Texture](Texture.html) [Texture](Texture.html)) { /* copy pixels in cache */ }
        int GetNextIndex() { return -1; /* Get next index to use in the cache */ }
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


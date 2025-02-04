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

# ObjectPool<T0> Constructor

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

public ObjectPool<T0>(Func<T> createFunc, Action<T> actionOnGet, Action<T>
actionOnRelease, Action<T> actionOnDestroy, bool collectionCheck, int
defaultCapacity, int maxSize);

### Parameters

createFunc | Used to create a new instance when the pool is empty. In most cases this will just be () => new T().  
---|---  
actionOnGet | Called when the instance is taken from the pool.  
actionOnRelease | Called when the instance is returned to the pool. This can be used to clean up or disable the instance.  
actionOnDestroy | Called when the element could not be returned to the pool due to the pool reaching the maximum size.  
collectionCheck | Collection checks are performed when an instance is returned back to the pool. An exception will be thrown if the instance is already in the pool. Collection checks are only performed in the Editor.  
defaultCapacity | The default capacity the stack will be created with.  
maxSize | The maximum size of the pool. When the pool reaches the max size then any further instances returned to the pool will be ignored and can be garbage collected. This can be used to prevent the pool growing to a very large size.  
  
### Description

Creates a new ObjectPool instance.

    
    
    using System.Text;
    using UnityEngine;
    using UnityEngine.Pool;  
      
    // This component returns the particle system to the pool when the OnParticleSystemStopped event is received.
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ReturnToPool : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystem](ParticleSystem.html) system;
        public IObjectPool<[ParticleSystem](ParticleSystem.html)> pool;  
      
        void Start()
        {
            system = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var main = system.main;
            main.stopAction = [ParticleSystemStopAction.Callback](ParticleSystemStopAction.Callback.html);
        }  
      
        void OnParticleSystemStopped()
        {
            // Return to the pool
            pool.Release(system);
        }
    }  
      
    // This example spans a random number of ParticleSystems using a pool so that old systems can be reused.
    public class PoolExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public enum PoolType
        {
            Stack,
            LinkedList
        }  
      
        public PoolType poolType;  
      
        // Collection checks will throw errors if we try to release an item that is already in the pool.
        public bool collectionChecks = true;
        public int maxPoolSize = 10;  
      
        IObjectPool<[ParticleSystem](ParticleSystem.html)> m_Pool;  
      
        public IObjectPool<[ParticleSystem](ParticleSystem.html)> Pool
        {
            get
            {
                if (m_Pool == null)
                {
                    if (poolType == PoolType.Stack)
                        m_Pool = new ObjectPool<[ParticleSystem](ParticleSystem.html)>(CreatePooledItem, OnTakeFromPool, OnReturnedToPool, OnDestroyPoolObject, collectionChecks, 10, maxPoolSize);
                    else
                        m_Pool = new LinkedPool<[ParticleSystem](ParticleSystem.html)>(CreatePooledItem, OnTakeFromPool, OnReturnedToPool, OnDestroyPoolObject, collectionChecks, maxPoolSize);
                }
                return m_Pool;
            }
        }  
      
        [ParticleSystem](ParticleSystem.html) CreatePooledItem()
        {
            var go = new [GameObject](GameObject.html)("Pooled [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var ps = go.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            ps.Stop(true, [ParticleSystemStopBehavior.StopEmittingAndClear](ParticleSystemStopBehavior.StopEmittingAndClear.html));  
      
            var main = ps.main;
            main.duration = 1;
            main.startLifetime = 1;
            main.loop = false;  
      
            // This is used to return ParticleSystems to the pool when they have stopped.
            var returnToPool = go.AddComponent<ReturnToPool>();
            returnToPool.pool = Pool;  
      
            return ps;
        }  
      
        // Called when an item is returned to the pool using Release
        void OnReturnedToPool([ParticleSystem](ParticleSystem.html) system)
        {
            system.gameObject.SetActive(false);
        }  
      
        // Called when an item is taken from the pool using Get
        void OnTakeFromPool([ParticleSystem](ParticleSystem.html) system)
        {
            system.gameObject.SetActive(true);
        }  
      
        // If the pool capacity is reached then any items returned will be destroyed.
        // We can control what the destroy behavior does, here we destroy the [GameObject](GameObject.html).
        void OnDestroyPoolObject([ParticleSystem](ParticleSystem.html) system)
        {
            Destroy(system.gameObject);
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Pool size: " + Pool.CountInactive);
            if ([GUILayout.Button](GUILayout.Button.html)("Create Particles"))
            {
                var amount = [Random.Range](Random.Range.html)(1, 10);
                for (int i = 0; i < amount; ++i)
                {
                    var ps = Pool.Get();
                    ps.transform.position = [Random.insideUnitSphere](Random-insideUnitSphere.html) * 10;
                    ps.Play();
                }
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

